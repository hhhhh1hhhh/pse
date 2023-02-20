// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import { Timer } from "./Timer";

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate({ subscriptions }: vscode.ExtensionContext) {
	const config = vscode.workspace.getConfiguration("PSE vscode extension");
	if (config.active === true) {
		//status bar items + command ID
		const playStatusBarItem: vscode.StatusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 3);
		const playTimerCommandId = "PSE.startTimer";
		const stopStatusBarItem: vscode.StatusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 3);
		const stopTimerCommandId = "PSE.stopTimer";
		const saveStatusBarItem: vscode.StatusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 2);
		const saveTimerCommandId = "PSE.saveTimer";

		//Timer
		const timerStatusBarItem: vscode.StatusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 1);
		const timerStatusBarIcon: string = `extensions-sync-enabled`;
		const timer = new Timer(timerStatusBarItem, timerStatusBarIcon);

		let sessionDate: Date = new Date(2023, 3, 1);

		//StatusBarItem command
		subscriptions.push(
			vscode.commands.registerCommand(playTimerCommandId, () => {
				timer.play();
				playStatusBarItem.hide();
				stopStatusBarItem.show();
				saveStatusBarItem.show();
				if (sessionDate.getFullYear() === 2023) {
					//처음 시작할때, 세션 날짜 설정
					sessionDate = new Date();
				}
			}),

			vscode.commands.registerCommand(stopTimerCommandId, () => {
				timer.stop();
				playStatusBarItem.show();
				stopStatusBarItem.hide();
			}),

			vscode.commands.registerCommand(saveTimerCommandId, async () => {
				const sessionSeconds: number = timer.getCueerentTime();
				//user가 x 누르거나 세션 계속할 경우, Timer 이전 상태로
				const prevTimerState: string = timer.getCurrentState();

				//사용자 설정으로 Timer stop
				if (prevTimerState === timer.timerStates.play) {
					timer.stop();
					stopStatusBarItem.hide();
				} else {
					playStatusBarItem.hide();
				}
				saveStatusBarItem.hide();
				timer.updateText("Closing...");

				//세션 continue 또는 stop : 메세지
				const response = await vscode.window.showErrorMessage(
					`Continue the session? Date: ${sessionDate.getUTCFullYear()}/${
						sessionDate.getUTCMonth() + 1
					}/${sessionDate.getUTCDate()} ${sessionDate.getHours()}:${sessionDate.getMinutes()} Time: ${timer.secToTime(
						sessionSeconds,
						true,
					)}`,
					"Continue",
					"Finish",
				);

				if (response === "Finish") {
					//default 세션 날짜
					timer.save();
					playStatusBarItem.show();
					timerStatusBarItem.text = "";
					sessionDate = new Date(2023, 3, 1);
					//https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/Date


				} else {
					//user가 세션을, x클릭 or continue 
					if (prevTimerState === timer.timerStates.play) {
						timer.play();
						stopStatusBarItem.show();
					} else {
						timer.updateText(`$(${timerStatusBarIcon})`);
						playStatusBarItem.show();
					}
					saveStatusBarItem.show();
				}
			}),
		);

		//PLAY StatusBarItem
		playStatusBarItem.command = playTimerCommandId;
		playStatusBarItem.text = `$(notebook-execute)`;
		playStatusBarItem.color = "LightSkyBlue";
		playStatusBarItem.show();
		subscriptions.push(playStatusBarItem);

		//STOP StatusBarItem
		stopStatusBarItem.command = stopTimerCommandId;
		stopStatusBarItem.text = `$(debug-pause)`;
		subscriptions.push(stopStatusBarItem);

		//SAVE StatusBarItem
		saveStatusBarItem.command = saveTimerCommandId;
		saveStatusBarItem.text = `$(debug-stop)`;
		subscriptions.push(saveStatusBarItem);

		//TIMER StatusBarItem
		timerStatusBarItem.show();
		subscriptions.push(timerStatusBarItem);
	}
}

	// 디버깅 시작 이벤트 (횟수)
let debugcount : number = 0;
	context.subscriptions.push(vscode.debug.onDidStartDebugSession(e => {
		debugcount += 1;
		vscode.window.showInformationMessage('Debug Start (WorkspaceFolder) : ' + e.workspaceFolder?.name + debugcount );
	})); 
	
	// 텍스트 에디터 선택 이벤트 (작성할 때 마다 업데이트) (최종 얼마나 작성했는지 알 수 있음)
	context.subscriptions.push(vscode.window.onDidChangeTextEditorSelection (e => {
		vscode.window.showInformationMessage('Change Text : ' + e.textEditor.document.getText());
	}));

	// 텍스트 에디터 변경 이벤트 (텍스트 변경 시 입력한 값을 가져옴 (하나씩))
	context.subscriptions.push(vscode.workspace.onDidChangeTextDocument (e => {
		vscode.window.showInformationMessage('Change Text(filename) : ' + e.contentChanges[0].text);
	}));

	//커맨드 등록
	context.subscriptions.push(vscode.commands.registerCommand('hello_world', _ => {
		vscode.window.showInformationMessage('hahaha'); 
		}));

	// 저장 시 횟수가 늘어남
let savecount : number = 0;
	context.subscriptions.push(vscode.workspace.onDidSaveTextDocument (e => {
		savecount += 1;
		vscode.window.showInformationMessage('sava file : ' + e.fileName + savecount);
	}));




	context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
export function deactivate() {}

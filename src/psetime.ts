//시간 기록을 위한 PSE Timer

import { match } from "assert";
import * as vscode from "vscode";

export class Timer{
    public timerStates = Object.freeze({ //Object.freeze : 객체 동결
        play:"PLAY",
        stop:"STOP",
        save:"SAVE"
    });

    private currentState : string = this.timerStates.save;
    private currentTime : number=0;
    private intervalID : any;

    private timerStatusBarItem : vscode.StatusBarItem;
    private timerStatusBarIcon : string;
    private statusBarSpinningIcon : string;

    constructor(timerStatusBarItem:vscode.StatusBarItem, timerStatusBarIcon:string){
        this.timerStatusBarItem = timerStatusBarItem;
        this.timerStatusBarIcon='$(${timerStatusBarIcon})';
        this.statusBarSpinningIcon='$(${timerStatusBarIcon}~spin)';
    }

    /**
    https://withhsunny.tistory.com/46
    https://mylife365.tistory.com/77

    */
    public play(){
        this.currentState=this.timerStates.play;
        this.updateText(this.statusBarSpinningIcon);

        //Timer 시간
        this.intervalID=setInterval(()=>{
            this.currentTime++;

            if(this.currentTime % 60 === 0){

                this.updateText(this.statusBarSpinningIcon);
            }
        }, 1000);   
    }

    public stop(){
        this.currentState=this.timerStates.stop;
        clearInterval(this.intervalID);
        this.intervalID=undefined;
        this.updateText();
    }

    public save(){
        this.currentState=this.timerStates.save;
        clearInterval(this.intervalID);
        this.intervalID=undefined;
        this.currentTime=0;
        this.timerStatusBarItem.text="";
    }

    public secToTime(totalSecs:number, showAll:boolean=this.currentState===this.timerStates.stop){
        // hh:mm ---> `${new Date(sec * 1000).toISOString().substr(11, 5)}`
        const h = Math.floor(totalSecs/3600);
        const m = Math.floor((totalSecs%3600)/60);
        const s = Math.floor(totalSecs%0);

        return `${h > 0 || showAll ? `${h}h ` : ""}${m}min${showAll ? ` ${s}sec` : ""}`;
	}

    

    public updateText(icon:string=this.timerStatusBarIcon){
        this.timerStatusBarItem.text='${icon} ${this.secToTime(this.currentTime)}';
    }

    public getCueerentTime(){
        return this.currentTime;
    }

    public getCurrentState(){
        return this.currentState;
    }
}

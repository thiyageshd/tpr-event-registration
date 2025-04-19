import { Injectable } from "@angular/core";
import {HttpClient } from '@angular/common/http'
import { AppConfig } from "../app-config";
import { RequestProfile } from "../model/registration-profile";


@Injectable({
    providedIn: 'root'
})

export class RegisterService {

    totalAmount!:number;
    selectedKilometer!:string;

    constructor(private httpClient:HttpClient){

    }

    getTotalAmount(){
        return this.totalAmount;
    }
    
    setTotalAmount(totalAmount:any){
        this.totalAmount=totalAmount;
    }

      getSelectedKilometer(){
        return this.selectedKilometer;
      }
    
      setSelectedKilometer(selectedKilometer:any){
        this.selectedKilometer=selectedKilometer;
      }

    registerUser(signUp: RequestProfile){
        const headerDict ={
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'X-API-Key':'test'
        }
        return this.httpClient.post<any>(AppConfig.registerUrl,signUp,{headers:headerDict});
    }

    getUser(phone_number: String, name:String){
        const headerDict ={
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'X-API-Key':'test'
        }
        return this.httpClient.get<any>(AppConfig.getUserUrl+"/"+phone_number+"/"+name,{headers:headerDict});
    }


}
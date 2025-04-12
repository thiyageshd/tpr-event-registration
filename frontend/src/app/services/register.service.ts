import { Injectable } from "@angular/core";
import {HttpClient } from '@angular/common/http'
import { AppConfig } from "../app-config";
import { RegistrationProfile } from "../model/registration-profile";


@Injectable({
    providedIn: 'root'
})

export class RegisterService {

    constructor(private httpClient:HttpClient){

    }

    registerUser(signUp: RegistrationProfile){
        return this.httpClient.post<any>(AppConfig.registerUrl,signUp);
    }

    getUser(data: any){
        return this.httpClient.post<any>(AppConfig.getUserUrl,data);
    }


}
import { Component } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { RequestProfile } from 'src/app/model/registration-profile';
import { RegisterService } from 'src/app/services/register.service';

@Component({
  selector: 'app-search-user',
  templateUrl: './search-user.component.html',
  styleUrls: ['./search-user.component.css']
})
export class SearchUserComponent {

  name:any;
  phoneNumber:any;
  email:any;
  requestProfile: RequestProfile = new RequestProfile;
  searchValues!: String[];

  constructor(private registerService:RegisterService){

  }

  onGetDetails(){
    this.searchValues[0]=this.requestProfile.name;
    this.searchValues[1]=this.requestProfile.phone_number;
    this.searchValues[2]=this.requestProfile.email;
    this.registerService.getUser(this.searchValues).subscribe( {
      next:(res)=>{
        console.log('User' , res);
        this.requestProfile=res;
      },
      error:()=>{
        console.log('failure');
      }
    });

  }

}

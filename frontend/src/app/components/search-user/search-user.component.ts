import { Component } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { RegistrationProfile } from 'src/app/model/registration-profile';
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
  registrationProfile: RegistrationProfile = new RegistrationProfile;
  searchValues!: String[];

  constructor(private registerService:RegisterService){

  }

  onGetDetails(){
    this.searchValues[0]=this.registrationProfile.name;
    this.searchValues[1]=this.registrationProfile.contactNumber;
    this.searchValues[2]=this.registrationProfile.email;
    this.registerService.getUser(this.searchValues).subscribe( {
      next:(res)=>{
        console.log('User' , res);
        this.registrationProfile=res;
      },
      error:()=>{
        console.log('failure');
      }
    });

  }

}

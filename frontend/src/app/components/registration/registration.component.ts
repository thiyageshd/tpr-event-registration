import { Component } from '@angular/core';
import { RegistrationProfile } from 'src/app/model/registration-profile';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NativeDateAdapter } from '@angular/material/core';
import { RegisterService } from 'src/app/services/register.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {

  constructor(private formBuilder:FormBuilder,
    private dateAdapter: NativeDateAdapter,
    private registerService:RegisterService) {}

  registrationProfile: RegistrationProfile = new RegistrationProfile;
  registrationForm !: FormGroup;

  ngOnInit(){
    this.registrationForm = this.formBuilder.group({
      registerId:[''],
      name:['',Validators.required],
      email:['',Validators.required],
      gender:['',Validators.required],
      contactNumber:['',Validators.required],
      dob:['',Validators.required],
      street:['',Validators.required],
      city:['',Validators.required],
      pincode:['',Validators.required],
      state:['',Validators.required],
      nameOnTheBib:['',Validators.required],
      tshirtSize:['',Validators.required],
      nameOfYourGroup:[''],
      breakfast:['',Validators.required],
      bloodGroup:['',Validators.required],
      emergencyContactName:['',Validators.required],
      emergencyContactNumber:['',Validators.required],
      termsAndCondition:['']
      
    });
  }

  onSubmit(){
    this.registrationProfile.name=this.registrationForm.get("name")?.value;
    this.registrationProfile.email=this.registrationForm.get("email")?.value;
    this.registrationProfile.contactNumber=this.registrationForm.get("contactNumber")?.value;
    this.registrationProfile.gender=this.registrationForm.get("gender")?.value;
    let date=this.dateAdapter.format(this.registrationForm.get("dob")?.value,'MM/dd/yyyy');
    this.registrationProfile.dob=date;
    this.registrationProfile.street=this.registrationForm.get("street")?.value;
    this.registrationProfile.city=this.registrationForm.get("city")?.value;
    this.registrationProfile.pincode=this.registrationForm.get("pincode")?.value;
    this.registrationProfile.state=this.registrationForm.get("state")?.value;
    this.registrationProfile.nameOnTheBib=this.registrationForm.get("nameOnTheBib")?.value;
    this.registrationProfile.tshirtSize=this.registrationForm.get("tshirtSize")?.value;
    this.registrationProfile.nameOfYourGroup=this.registrationForm.get("nameOfYourGroup")?.value;
    this.registrationProfile.breakfast=this.registrationForm.get("breakfast")?.value;
    this.registrationProfile.bloodGroup=this.registrationForm.get("bloodGroup")?.value;
    this.registrationProfile.emergencyContactName=this.registrationForm.get("emergencyContactName")?.value;
    this.registrationProfile.emergencyContactNumber=this.registrationForm.get("emergencyContactNumber")?.value;
    this.registrationProfile.termsAndCondition=this.registrationForm.get("termsAndCondition")?.value;
    this.registerService.registerUser(this.registrationProfile).subscribe( {
      next:(res)=>{
        console.log('Saved Sucessfully.');
      },
      error:()=>{
        console.log('failure');
      }
    });

}

onBack(){

}
  
}

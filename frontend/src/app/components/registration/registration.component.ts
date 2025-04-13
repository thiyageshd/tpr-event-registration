import { Component } from '@angular/core';
import { RegistrationProfile, RequestProfile } from 'src/app/model/registration-profile';
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
  requestProfile: RequestProfile = new RequestProfile;
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
    this.requestProfile.name=this.registrationForm.get("name")?.value;
    this.requestProfile.email=this.registrationForm.get("email")?.value;
    this.requestProfile.phone_number=this.registrationForm.get("contactNumber")?.value;
    this.requestProfile.gender=this.registrationForm.get("gender")?.value;
    let date=this.dateAdapter.format(this.registrationForm.get("dob")?.value,'MM/dd/yyyy');
    this.requestProfile.dob=date;
    this.requestProfile.street=this.registrationForm.get("street")?.value;
    this.requestProfile.city=this.registrationForm.get("city")?.value;
    this.requestProfile.pincode=this.registrationForm.get("pincode")?.value;
    this.requestProfile.state=this.registrationForm.get("state")?.value;
    this.requestProfile.name_on_the_bib=this.registrationForm.get("nameOnTheBib")?.value;
    this.requestProfile.event_type='21km';
    this.requestProfile.t_shirt_size=this.registrationForm.get("tshirtSize")?.value;
    this.requestProfile.name_of_your_group=this.registrationForm.get("nameOfYourGroup")?.value;
    this.requestProfile.breakfast=this.registrationForm.get("breakfast")?.value;
    this.requestProfile.blood_group=this.registrationForm.get("bloodGroup")?.value;
    this.requestProfile.emergency_contact_name=this.registrationForm.get("emergencyContactName")?.value;
    this.requestProfile.emergency_contact_number=this.registrationForm.get("emergencyContactNumber")?.value;
    this.requestProfile.terms_and_condition=this.registrationForm.get("termsAndCondition")?.value;
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

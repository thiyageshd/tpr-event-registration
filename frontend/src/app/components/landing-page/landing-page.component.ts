import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RegisterService } from 'src/app/services/register.service';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent {

  constructor(private router: Router,
  private registerService:RegisterService){

  }
  selectedOption!:string;
  selectedAmount:number=0;
  totalAmount:number=42.43;

  onNext(){
    this.router.navigate(["registration"]);
    this.registerService.setTotalAmount(this.totalAmount);
    this.registerService.setSelectedKilometer(this.selectedOption);
    

  }
  changeOption(){
    this.totalAmount=42.43;
    console.log(this.selectedOption);
    if(this.selectedOption === '5km'){
      this.selectedAmount=499.00;
    }else if (this.selectedOption === '5km-Timed'){
      this.selectedAmount=599.00;
    }else if(this.selectedOption === '10km'){
      this.selectedAmount=899.00;
    }else if (this.selectedOption === '21km'){
      this.selectedAmount=999.00;
    }
    this.totalAmount+=this.selectedAmount;
  }

}

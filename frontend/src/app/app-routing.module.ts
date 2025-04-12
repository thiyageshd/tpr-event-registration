import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegistrationComponent } from './components/registration/registration.component';
import { SearchUserComponent } from './components/search-user/search-user.component';

const routes: Routes = [
  { path: '', redirectTo: '/registration', pathMatch: 'full' },
  { path: 'registration', component: RegistrationComponent },
  { path: 'search-user', component: SearchUserComponent },
  
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

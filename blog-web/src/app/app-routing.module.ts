import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login/login.component';
import { BlogComponent } from './blog/blog/blog.component';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/blog', pathMatch: 'full' }, 
  { path: 'blog', component: BlogComponent, canActivate: [AuthGuard] },
  // { path: 'blog', component: BlogComponent},
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

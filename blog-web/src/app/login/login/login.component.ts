import { Component, OnInit } from '@angular/core';
import { BlogPageService } from '../blog-page.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  login = true
  registerForm: FormGroup;
  message:any
  errorMsg: any

  constructor(private authService: AuthService,
            private blogSevice:BlogPageService,
              private fb: FormBuilder,
              private router: Router) 
  { 
    this.loginForm = this.fb.group({
      userName: ['', Validators.required],
      password: ['', Validators.required]
    });


    this.registerForm = this.fb.group({
      firstName: ['', Validators.required],
      lastName: [''],
      userName: ['', Validators.required],
      password: ['', Validators.required],
      email: ['', Validators.required]
    });
  }

  ngOnInit(): void {
  }

  onLogin() {
    this.authService.login(); // Log in the user
    this.router.navigate(['/blog']); // Redirect to home after login
  }

  onSubmit() {
    if (this.login){
      this.blogSevice.loginUser(this.loginForm.value).subscribe(response =>{
        console.log(response)
        this.message = response.message
        this.loginForm.reset();
        // this.router.navigate(['/blog'])
        this.onLogin()
        
      }
      ,error =>{
        this.errorMsg = error.error.err
        console.log(error.error.err)
    }
    )
    }
    else{
      this.blogSevice.registerUser(this.registerForm.value).subscribe(response =>{
        console.log(response.message)
        
        this.changeLoginValue()
        this.registerForm.reset();
        // this.login = !this.login
        this.message = response.message
      }
    ,error =>{
        this.errorMsg = error.error.err
        console.log(error.error.err)
    });
    }
   
  }

  changeLoginValue(){
    this.login = !this.login
    this.message = ''
    this.errorMsg = ''

  }

}

import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRoute } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router, private activatedRoute: ActivatedRoute) {
    this.activatedRoute.params.subscribe(data => {
      console.log("guard params");
      this.authService.isAuthenticated.subscribe(res => {
        this.isAthenticated = res
      })
    })
  }

  canActivate(): boolean {
    if (this.authService.isLoggedIn()) {
      return true;
    } else {
      this.router.navigate(['/login']);
      return false;
    }
  }
}

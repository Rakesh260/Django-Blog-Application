import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private loggedIn = false;

  // Call this method to log in the user
  login() {
    this.loggedIn = true;
  }

  // Call this method to log out the user
  logout() {
    this.loggedIn = false;
  }

  // Check if the user is logged in
  isLoggedIn(): boolean {
    return this.loggedIn;
  }
}

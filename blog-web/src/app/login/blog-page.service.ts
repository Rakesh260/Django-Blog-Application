import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BlogPageService {
  withCredentials: any
  
  private baseUrl = 'http://127.0.0.1:8004/blog'

  constructor(private http: HttpClient) { }

  loginUser(data:any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/login`,data, {withCredentials: true});
  }
  
  registerUser(data:any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/register`,data);
  }
  
  // getBlogsData(data:any)

  createBlog(data:any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/create-post-blog`,data, {withCredentials: true});
  }


  getBlogsData(data:any): Observable<any> {
    console.log(data)

    let params = new HttpParams();
    if (data) {
      Object.keys(data).forEach(key => {
        params = params.append(key, data[key]);
      });
    }
    return this.http.get<any>(`${this.baseUrl}/create-post-blog`, { params: params,withCredentials: true });
  }

}

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from '../models/user';
import { Product } from '../models/product';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AdvertiseService {

  private advertiseUrl = "http://35.198.220.113:9100/"

  constructor(private http: HttpClient) {

  }

  getAllPackages(user:User): Observable<any>{
    let url = this.advertiseUrl+"/packagesApi"
    let body = JSON.stringify({ "email":user.email,"password":user.password, "mobile":user.mobile });
    const options = {
      headers: new HttpHeaders().append('Content-Type', 'application/json')
                                .append('Access-Control-Allow-Origin','*'),
      mode: 'no-cors'

    }
    console.log("Done");
    return this.http.get<any>(url);
  }
}

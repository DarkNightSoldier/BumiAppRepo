import { Injectable } from "@angular/core";
import { Router } from "@angular/router";
import { environment } from "src/environments/environment";
import { HttpClient } from "@angular/common/http";
import { Product } from '../models/product.model';

@Injectable({ providedIn: 'root' })
export class ProductService {
    
    endpoint = environment.endpoint;
    constructor(private http: HttpClient, private router: Router) {}

    submitProduct(
        id: number, 
        nombre: string,
        stock: number, 
        url_img: string, 
        precio_antes_impuesto: number, 
        impuesto_porcentaje: number, 
        descuento: number
    ){
        const productData: Product = {
            id: id, 
            nombre: nombre,
            stock: stock, 
            url_img: url_img, 
            precio_antes_impuesto: precio_antes_impuesto, 
            impuesto_porcentaje: impuesto_porcentaje, 
            descuento: descuento
        }
        console.log(this.endpoint + "/api/articulo/crear_nuevo_articulo");
        console.log("Data that will be sent to server: ")
        console.log(productData);
        return this.http.post(this.endpoint + "/api/articulo/crear_nuevo_articulo", productData)
    }


}
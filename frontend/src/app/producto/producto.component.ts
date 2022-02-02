import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ProductService } from '../services/product.services';

@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})
export class ProductoComponent implements OnInit {

  constructor(private productService: ProductService) { }
  form: FormGroup;
  success: boolean = false;
  isLoading: boolean = false;
  error: boolean = false;


  ngOnInit(): void {
    this.form = new FormGroup({
      id: new FormControl(null, {validators: [Validators.required]}), 
      nombre: new FormControl(null, {validators: [Validators.required]}),
      stock: new FormControl(null, {validators: [Validators.required]}), 
      url_img: new FormControl(null, {validators: [Validators.required]}), 
      precio_antes_impuesto: new FormControl(null, {validators: [Validators.required]}), 
      impuesto_porcentaje: new FormControl(null, {validators: [Validators.required]}), 
      descuento: new FormControl(null, {validators: [Validators.required]})
    })
  }

  onSubmit(){
    if(this.form.invalid){
      return;
    }
    this.isLoading = true;
    this.success = false;
    this.error = false;
    let values = this.form.value;
    this.productService.submitProduct(
      values.id, 
      values.nombre,
      values.stock, 
      values.url_img, 
      values.precio_antes_impuesto, 
      values.impuesto_porcentaje, 
      values.descuento
    ).subscribe(
      (data) => {
        this.isLoading = false;
        this.success = true;
        this.form.reset();
      }, 
      (err) => {  
        this.isLoading = false;
        this.error = true;
      }
    )
  
  }

}

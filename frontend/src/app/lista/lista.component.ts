import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ProductService } from '../services/product.services';

@Component({
  selector: 'app-lista',
  templateUrl: './lista.component.html',
  styleUrls: ['./lista.component.css']
})
export class ListaComponent implements OnInit {

  isLoading: boolean = false;
  error: boolean = false;
  success = false;

  id: string = "0";
  nombre: string = "Detergent IBEMEX"
  stock: string = "200"
  url_img: string = "https://target.scene7.com/is/image/Target/GUEST_aa6c5c65-36c3-4de6-a255-bb077424f252?wid=488&hei=488&fmt=pjpeg"
  precio_antes_impuesto: string = "200"
  impuesto_porcentaje: string = "0.19"
  descuento: string = "0.7"

  constructor(private productService: ProductService) { }
  form: FormGroup;
  ngOnInit(): void {
    this.form = new FormGroup({
      id: new FormControl(null, {validators: [Validators.required]}), 
    });
  }

  onSubmit(){
    if(this.form.invalid){
      return;
    }
    this.success = false;
    this.error = false;
    let values = this.form.value;
    this.productService.getProduct(
      values.id
    ).subscribe(
      (data: any) => {
        console.log(data);
        let datos = data.datos;
        this.success = true;
        this.id = datos.id
        this.nombre = datos.nombre
        this.stock = datos.stock
        this.url_img = datos.url_img
        this.precio_antes_impuesto = datos.precio_antes_impuesto 
        this.impuesto_porcentaje = datos.impuesto_porcentaje
        this.descuento = datos.descuento
      },
      (err) => {
        this.error = true;
      }
    )
  }

}

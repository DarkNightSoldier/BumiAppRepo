import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './main/main.component';
import { PedirComponent } from './pedir/pedir.component';
import { ProductoComponent } from './producto/producto.component';

const routes: Routes = [
  {path : "", component : MainComponent},
  {path: "pedir", component: PedirComponent},
  {path: "product", component: ProductoComponent},
  {path: "**", pathMatch:'full', redirectTo: ""}
  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListaComponent } from './lista/lista.component';
import { MainComponent } from './main/main.component';
import { PedirComponent } from './pedir/pedir.component';
import { ProductoComponent } from './producto/producto.component';

const routes: Routes = [
  {path : "", component : MainComponent},
  {path: "pedir", component: PedirComponent},
  {path: "product", component: ProductoComponent},
  {path: "buscar", component: ListaComponent},
  {path: "**", pathMatch:'full', redirectTo: ""}
  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
<<<<<<< HEAD
=======

>>>>>>> 1c8fd66adc6e3b59e89cbf60b2a313df4ad5f14f

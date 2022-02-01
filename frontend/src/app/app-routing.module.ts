import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './main/main.component';
import { PedirComponent } from './pedir/pedir.component';

const routes: Routes = [
  {path: "pedir", component: PedirComponent},
  {path : "home", component : MainComponent},
  {path: "**", pathMatch:'full', redirectTo: 'home' }
  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const app_routes = RouterModule.forRoot(app_routes);

import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { UploadImageComponent } from './upload-image/upload-image.component';
import { GasSensorComponent } from './gas-sensor/gas-sensor.component';
import { ResultsComponent } from './results/results.component';

export const routes: Routes = [
  { path: '', component: DashboardComponent },
  { path: 'upload-image', component: UploadImageComponent },
  { path: 'gas-sensor', component: GasSensorComponent },
  { path: 'results', component: ResultsComponent },
];


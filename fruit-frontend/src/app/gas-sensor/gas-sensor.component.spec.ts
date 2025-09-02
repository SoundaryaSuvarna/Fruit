import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GasSensorComponent } from './gas-sensor.component';

describe('GasSensorComponent', () => {
  let component: GasSensorComponent;
  let fixture: ComponentFixture<GasSensorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GasSensorComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GasSensorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FullContentDialogComponent } from './full-content-dialog.component';

describe('FullContentDialogComponent', () => {
  let component: FullContentDialogComponent;
  let fixture: ComponentFixture<FullContentDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FullContentDialogComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FullContentDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

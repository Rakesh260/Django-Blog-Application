import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA,MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-full-content-dialog',
  templateUrl: './full-content-dialog.component.html',
  styleUrls: ['./full-content-dialog.component.css']
})
export class FullContentDialogComponent {
  blogPastData:any

  constructor(@Inject(MAT_DIALOG_DATA) public data: any,
  public dialogRef: MatDialogRef<FullContentDialogComponent> )
   {
    this.blogPastData = data.blog
    console.log('dd',this.blogPastData)
   }
   ngOnInit(): void {
  }
}

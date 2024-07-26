import { Component, Inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MAT_DIALOG_DATA,MatDialogRef } from '@angular/material/dialog';
import { BlogPageService } from '../login/blog-page.service';

@Component({
  selector: 'app-add-new-blog',
  templateUrl: './add-new-blog.component.html',
  styleUrls: ['./add-new-blog.component.scss']
})
export class AddNewBlogComponent  {

  createBlogForm:FormGroup
  errorMsg: any

  constructor(@Inject(MAT_DIALOG_DATA) public data: any,
  public dialogRef: MatDialogRef<AddNewBlogComponent> ,
  private fb: FormBuilder,
  private blogSevice:BlogPageService)
   {
    this.createBlogForm = this.fb.group({
      title: ['', Validators.required],
      content: ['', Validators.required]
    });
   }

  ngOnInit(): void {
  }

  onSubmit(){
    this.blogSevice.createBlog(this.createBlogForm.value).subscribe(response =>{
      this.dialogRef.close();
      
    }
    ,error =>{
      console.log(error)
      this.errorMsg = error.error

  })
  }




}

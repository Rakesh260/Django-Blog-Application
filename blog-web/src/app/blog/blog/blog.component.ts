import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Observable } from 'rxjs';
import { AddNewBlogComponent } from 'src/app/add-new-blog/add-new-blog.component';
import { FullContentDialogComponent } from 'src/app/full-content-dialog/full-content-dialog.component';
import { BlogPageService } from 'src/app/login/blog-page.service';
@Component({
  selector: 'app-blog',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.scss']
})
export class BlogComponent implements OnInit {

data: any

pageLength = 6
totalLength:any
pageIndex = 1
filters: any
constructor(private dialog: MatDialog,
  private blogSevice:BlogPageService
) {
  this.getBlogsData()
}

ngOnInit(): void {
}


loadProducts(pageIndex: number, pageSize: number){
  this.pageLength =pageSize
  this.pageIndex = pageIndex + 1
  this.getBlogsData() 
}

getFilters(){
  this.filters = {}
    this.filters.pageLength = this.pageLength
    this.filters.pageIndex = this.pageIndex

  return this.filters 
}

openDialog(blog: any) {
  const dialogRef = this.dialog.open(FullContentDialogComponent, {
    data: { blog },
    panelClass: 'custom-dialog-class' 
  });
  dialogRef.afterClosed().subscribe(result => {
    this.getBlogsData() 
  });
}

addNewBlog(){
  const dialogRef = this.dialog.open(AddNewBlogComponent, {
    panelClass: 'custom-dialog-class' 
  });
  dialogRef.afterClosed().subscribe(result => {
    this.getBlogsData() 
  });
}

getBlogsData(){

  this.blogSevice.getBlogsData(this.getFilters()).subscribe(response =>{
    this.data = response.data
    this.totalLength = response.count
    
  }
  ,error =>{
    console.log(error)

})
}
}

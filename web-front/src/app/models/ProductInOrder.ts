import {Product} from "./product";

export class ProductInOrder {
    productId: number;
    productName: string;
    productPrice: number;
    productStock: number;
    productDescription: string;
    count: number;

    constructor(product:Product, quantity = 1){
        this.productId = product.id;
        this.productName = product.package_name;
        this.productPrice = product.price;
        this.productStock = product.available_qty;
        this.productDescription = product.package_description;
        this.count = quantity;
    }
}
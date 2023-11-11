/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.soal2d_clo;

/**
 *
 * @author Nugee
 */
public class OrderDetail {
    private int productID;
    private int qty;
    private double unitPrice;
    private double price;

    public OrderDetail(int productID, int qty, double unitPrice) {
        this.productID = productID;
        this.qty = qty;
        this.unitPrice = unitPrice;
        this.price = qty * unitPrice;
    }

    // Getter methods

    public int getProductID() {
        return productID;
    }

    public int getQty() {
        return qty;
    }

    public double getUnitPrice() {
        return unitPrice;
    }

    public double getPrice() {
        return price;
    }
}

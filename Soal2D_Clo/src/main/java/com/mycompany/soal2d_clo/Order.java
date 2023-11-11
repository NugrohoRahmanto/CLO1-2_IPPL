/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.soal2d_clo;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 *
 * @author Nugee
 */
public class Order {
    private int orderID;
    private Date orderDate;
    private String orderTime;
    private double orderTotal;
    private double orderMoney;
    private double orderChange;
    private List<OrderDetail> orderDetails;

    public Order(int orderID, Date orderDate, String orderTime, double orderMoney) {
        this.orderID = orderID;
        this.orderDate = orderDate;
        this.orderTime = orderTime;
        this.orderMoney = orderMoney;
        this.orderDetails = new ArrayList<>();
    }

    public void addOrderDetail(OrderDetail orderDetail) {
        orderDetails.add(orderDetail);
        orderTotal += orderDetail.getPrice();
        calculateChange();
    }

    private void calculateChange() {
        orderChange = orderMoney - orderTotal;
    }

    // Getter methods

    public int getOrderID() {
        return orderID;
    }

    public Date getOrderDate() {
        return orderDate;
    }

    public String getOrderTime() {
        return orderTime;
    }

    public double getOrderTotal() {
        return orderTotal;
    }

    public double getOrderMoney() {
        return orderMoney;
    }

    public double getOrderChange() {
        return orderChange;
    }

    public List<OrderDetail> getOrderDetails() {
        return orderDetails;
    }
}

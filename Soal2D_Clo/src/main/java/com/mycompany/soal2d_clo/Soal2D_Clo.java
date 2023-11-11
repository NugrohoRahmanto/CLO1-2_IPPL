/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.soal2d_clo;
import java.util.Date;
/**
 *
 * @author Nugee
 */
public class Soal2D_Clo {

    public static void main(String[] args) {
        OrderDetail orderDetail1 = new OrderDetail(1, 2, 10.0);
        OrderDetail orderDetail2 = new OrderDetail(2, 1, 5.0);

        Order order = new Order(1, new Date(), "8:00", 30.0);
        order.addOrderDetail(orderDetail1);
        order.addOrderDetail(orderDetail2);

        // Menampilkan informasi pesanan dan detail pesanan
        System.out.println("Order ID: " + order.getOrderID());
        System.out.println("Order Date: " + order.getOrderDate());
        System.out.println("Order Time: " + order.getOrderTime());
        System.out.println("Order Total: " + order.getOrderTotal());
        System.out.println("Order Money: " + order.getOrderMoney());
        System.out.println("Order Change: " + order.getOrderChange());

        System.out.println("\nOrder Details:");
        for (OrderDetail detail : order.getOrderDetails()) {
            System.out.println("Product ID: " + detail.getProductID());
            System.out.println("Quantity: " + detail.getQty());
            System.out.println("Unit Price: " + detail.getUnitPrice());
            System.out.println("Price: " + detail.getPrice());
            System.out.println("---------------------");
        }
    }
}

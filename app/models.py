from django.db import models
from django.utils import timezone

class Product(models.Model):
    PRODUCT_TYPES = [
        ('base', 'Base'),
        ('seasonal', 'Seasonal'),
        ('bulk', 'Bulk'),
        ('premium', 'Premium'),
    ]
    
    name = models.CharField(max_length=128, null=False, blank=False)
    type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='base')
    base_price = models.FloatField(default=0)
    
    def get_price(self, quantity = 1):
        if type == 'seasonal':
            current_month = timezone.now().month
            # winter months [12,1,2]
            if current_month in [12, 1, 2]:
                return self.base_price * 0.8
            return self.base_price
            
        elif self.type == 'bulk':
            if quantity >= 51:
                return self.base_price * 0.85
            elif quantity >= 21:
                return self.base_price * 0.90
            elif quantity >= 10:
                return self.base_price * 0.95
            else:
                return self.base_price
            
        elif self.type == 'premium':
            # 15% markup
            return self.base_price * 1.15
        return self.base_price
    

class Discount(models.Model):
    DISCOUNT_TYPES = [
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount'),
        ('tiered', 'Tiered'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=DISCOUNT_TYPES)
    value = models.FloatField()
    priority = models.IntegerField()

    def apply_discount(self, total):
        if self.type == 'percentage':
            return total * (1 - self.value / 100)
        elif self.type == 'fixed':
            return max(0, total - self.value)
        elif self.type == 'tiered':
            if total > 1000:
                return total * 0.90
            elif total >= 500:
                return total * 0.95
            return total
        return total


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    discounts = models.ManyToManyField(Discount, blank=True)

    def calculate_total(self):
        total = sum([item.get_subtotal() for item in self.items.all()])
        for discount in sorted(self.discounts.all(), key=lambda d: d.priority):
            total = discount.apply_discount(total)
        return total
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete= models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    
    def get_subtotal(self):
        return self.product.get_price(self.quantity) * self.quantity




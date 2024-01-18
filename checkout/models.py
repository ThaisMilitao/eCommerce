from django.db import models
from django.conf import settings

# Create your models here.
class CartItemManager(models.Manager):
    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity += 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(cart_key=cart_key, product=product, price=product.price)
        return cart_item, created

class CartItem(models.Model):
    cart_key = models.CharField('Cart key', max_length=40, db_index=True)
    product = models.ForeignKey('catalog.Product', verbose_name='Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity', default = 1)
    price = models.DecimalField("Price", max_digits=8, decimal_places=2)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Cart Item'
        # verbose_name_plural = 'Carts Itens'
        unique_together = (('cart_key', 'product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)
    
class OrderManager(models.Manager):
    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=order, 
                quantity=cart_item.quantity, product=cart_item.product,
                price=cart_item.price)

class Order(models.Model):
    STATUS_CHOICES = (
        (0,'Aguardando Pagamento'),
        (1,'Concluida'),
        (2,'Cancelada'),
    )
    PAYMENT_OPTION_CHOICES =(
        ('deposit', 'Deposit')
        ('pagseguro', 'PagSeguro'),
        ('paypal', 'PayPal')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'User', on_delete=models.CASCADE)
    status = models.IntegerField('status', choices=STATUS_CHOICES, default=0, blank=True)
    payment_option = models.CharField('Payment Option', choices=PAYMENT_OPTION_CHOICES, max_length=20, defaul='deposit')

    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now_add=True)
    
    objects = OrderManager()

    class Meta:
        verbose_name = 'Order'
        # verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'Order #{self.pk}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Order', related_name='Items',on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', verbose_name='Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity', default = 1)
    price = models.DecimalField("Price", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Order Item'
        # verbose_name_plural = 'OrderItems'

    def __str__(self):
        return f'[{self.order}] {self.product}'

def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()
    
models.signals.post_save.connect(post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')
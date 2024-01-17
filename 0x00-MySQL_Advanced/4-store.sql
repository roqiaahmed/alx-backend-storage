-- decreases the quantity of an item after adding a new order
DROP TRIGGER IF EXISTS after_orders_insert;
CREATE TRIGGER after_orders_insert 
AFTER INSERT ON orders 
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
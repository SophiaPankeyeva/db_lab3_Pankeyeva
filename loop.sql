DO $$
 DECLARE
     food_type   food_types.food_type_id%TYPE;
     food_type_name food_types.food_type_name%TYPE;
 BEGIN
     food_type := 10;
     food_type_name := 'Dish';
     FOR counter IN 1..10
         LOOP
             INSERT INTO food_types(food_type_id, food_type_name)
            VALUES (counter + food_type, food_type_name || counter);
         END LOOP;
 END;
 $$

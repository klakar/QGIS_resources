# Random points in polygon

This code is used in a QGIS geometry generator for polygons.

It creates random points inside polygons in a vector layer. The amount of points is somewhat controlled by a variable/number.
In the code it is exemplified by a field name you need to replace with your own values in order to get the code to work.

```
geom_from_wkt(
  -- start a WKT MULTIPOINT
  'MULTIPOINT (' ||
    -- and in here build a coordinate list
    array_to_string( 
      array_remove_all(
        array_foreach(
          -- n times make a random point
          -- then if it is within the geometry return its coordinates
          -- otherwise return an empty string
	  
	  -- here is the attribute field name for the number of points
          generate_series(1, "num_points"),  -- unused array just for making a loop
          with_variable(
            'rnd_p', 
            make_point(
              randf(x_min($geometry), x_max($geometry)),
              randf(y_min($geometry), y_max($geometry))
            ),
            if(
              intersects(@rnd_p, $geometry),
              to_string(x(@rnd_p)) || ' ' || to_string(y(@rnd_p)),
              ''
            )
          )
        )  -- array_foreach, loop
      , '')  -- array_remove_all, remove all empty strings
    , ',')  -- array_to_string, convert all the coordinates into a single string
  || ')'  -- close the WKT MULTIPOINT
)  -- and make it an actual geometry
```

In the code on row six, there's reference to a field name (*"num_points"*). 
If you want to have a fixed value for the number of random points in each polygon, just replace this variable with that number.
You could also calculate a value for each feature and replace the field name with the code for that.

## Known Issues
Note that the number is the number of attempts that is made to generate random points in the polygon.
If any generated point is outside the polygon, no new attempt will be made to replace it, and it will simply be excluded from the result.

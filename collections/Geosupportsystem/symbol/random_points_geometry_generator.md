# Random points in polygon

This code is used in a QGIS geometry generator for polygons.

```
geom_from_wkt('MULTIPOINT (' ||
 array_to_string( 
  array_remove_all( 
    array_foreach( generate_series(1,
    
    "num_points"
    
    ), 
     with_variable( 'rnd_p', make_point(  randf( x_min( $geometry), x_max( $geometry)),
			   randf( y_min( $geometry), y_max( $geometry))
			  ),
			  if( within( @rnd_p, $geometry),
	             to_string(x(@rnd_p)) || ' ' || to_string(y(@rnd_p)),
			   '')
               )
    ),''
  ),','
) || ')'
)
```

In the code on row six, there's reference to a field name (*"num_points"*). 
If you want to have a fixed value for the number of random points in each polygon, just replace this variable with that number.
You could also calculate a value for each feature and replace the field name with the code for that.

##Known Issues
Note that the number is the number of attempts that is made to generate random points in the polygon.
If any generated point is outside the polygon, no new attempt will be made to replace it, and it will simply be excluded from the result.

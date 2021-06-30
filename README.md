# polar_grapher
a simple module that draws polar functions using `pygame`.


## usage
It is fairly simple to use this module. There are two self-explanatory functions: `draw` and `draw_parametric`.


#### 1. draw(eq, plane_size=(800, 800), continuity=0.005, color=PINK)

graphs a polar function with the form <img src="https://render.githubusercontent.com/render/math?math=r = f(t)">.
 
 * `eq` is a string, and the equation of the function that is going to be graphed. It *must* be exactly written in the form `"r = func"` (mind the spaces) and `func` must only contain the variable `t` (theta).
For example: to graph the archimedean spiral, <img src="https://render.githubusercontent.com/render/math?math=r = 100 \cdot \theta">, `eq` must be `"r = 100*t"`.

* `plane_size` is a tuple containing the scales of the coordinate plane (width, height). It is set to `(800, 800) `by default.

* `continuity` is a value that determines the amount of points drawn on the graph. If continuity were to set to a lower value  than the detail of the graph would increase as more points would be drawn, but the drawing process would be slower and vice versa. Set to `0.005` by default
* `color` is the color (RGB) of the graph. Set to `PINK` (pink) by default.

#### 2.  draw_parametric(eq1, eq2, plane_size=(800, 800), continuity=0.001, color=PINK)

Same as `draw` but it graphs parametric polar functions.

Since both functions are very similar I will give you an example:

To graph the tractrix spiral: <img src="https://render.githubusercontent.com/render/math?math=\displaystyle {\begin{cases}r=100 \cdot \cos(t)\\\theta =\tan(t)-t\end{cases}}">

`eq1` must be `"r = 100*cos(t)"` , and `eq2` must be `"t = tan(t)-t"`

As we see `eq1` must be <img src="https://render.githubusercontent.com/render/math?math=r(t)"> and `eq2` must be <img src="https://render.githubusercontent.com/render/math?math=\theta(t)">.

Other parameters are the same as they are in `draw`.


 ## important notes
 * You can also graph piecewise polar functions using pythonic expressions like:
 ```
 draw("r = 100 if t > 4 else 50")
 ```
 * Remember to check out the examples.


## screenshots

![atomic](screenshots/atomic.png?raw=true "Title")

<img src="https://render.githubusercontent.com/render/math?math=r = \frac{\theta}{\theta-13}">

*atomic spiral*


![strawberry](screenshots/strawberry.png?raw=true "Title")

<img src="https://render.githubusercontent.com/render/math?math=r = 100(\cos(\theta))^40%2B100\cos(\theta)%2B100">

I have no idea what this graph is called. I found it playing and testing the module. I called it *strawberry*.

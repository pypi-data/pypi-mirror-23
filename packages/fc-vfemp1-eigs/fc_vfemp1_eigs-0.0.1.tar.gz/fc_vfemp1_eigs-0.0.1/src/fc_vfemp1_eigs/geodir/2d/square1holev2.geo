DefineConstant[
  N = {10, Name "Input/1Points "},
  L = {1,  Name "Input/2Rect "},
  r = {0.1, Name "Input/3Radius"}
];

h=r/N;
Point(1) = {-L,-L,0,h};
Point(2) = {L,-L,0,h};
Point(3) = {L,L,0,h};
Point(4) = {-L,L,0,h};
Point(5) = {L,0,0,h};
Point(6) = {0,L,0,h};
Point(7) = {-L,0,0,h};
Point(8) = {0,-L,0,h};


Point(10) = {0,0,0,h};
Point(11) = {r,0,0,h};
Point(12) = {0,r,0,h};
Point(13) = {-r,0,0,h};
Point(14) = {0,-r,0,h};
Theta=Pi/4;
Point(15) = {r*Cos(Theta),r*Sin(Theta),0,h};
Theta=3*Pi/4;
Point(16) = {r*Cos(Theta),r*Sin(Theta),0,h};
Theta=5*Pi/4;
Point(17) = {r*Cos(Theta),r*Sin(Theta),0,h};
Theta=7*Pi/4;
Point(18) = {r*Cos(Theta),r*Sin(Theta),0,h};
//+
Line(9) = {11, 5};
//+
Line(10) = {15, 3};
//+
Line(11) = {12, 6};
//+
Line(12) = {16, 4};
//+
Line(13) = {13, 7};
//+
Line(14) = {17, 1};
//+
Line(15) = {14, 8};
//+
Line(16) = {18, 2};
//+
Circle(17) = {11, 10, 15};
//+
Circle(18) = {15, 10, 12};
//+
Circle(19) = {12, 10, 16};
//+
Circle(20) = {16, 10, 13};
//+
Circle(21) = {13, 10, 17};
//+
Circle(22) = {17, 10, 14};
//+
Circle(23) = {14, 10, 18};
//+
Circle(24) = {18, 10, 11};
//+
Line(25) = {1, 8};
//+
Line(26) = {8, 2};
//+
Line(27) = {2, 5};
//+
Line(28) = {5, 3};
//+
Line(29) = {3, 6};
//+
Line(30) = {6, 4};
//+
Line(31) = {4, 7};
//+
Line(32) = {7, 1};
//+
Line Loop(1) = {9, 28, -10, -17};
//+
Plane Surface(1) = {1};
//+
Line Loop(2) = {10, 29, -11, -18};
//+
Plane Surface(2) = {2};
//+
Line Loop(3) = {30, -12, -19, 11};
//+
Plane Surface(3) = {3};
//+
Line Loop(4) = {12, 31, -13, -20};
//+
Plane Surface(4) = {4};
//+
Line Loop(5) = {13, 32, -14, -21};
//+
Plane Surface(5) = {5};
//+
Line Loop(6) = {22, 15, -25, -14};
//+
Plane Surface(6) = {6};
//+
Line Loop(7) = {23, 16, -26, -15};
//+
Plane Surface(7) = {7};
//+
Line Loop(8) = {9, -27, -16, 24};
//+
Plane Surface(8) = {8};
//+
Physical Line(1) = {31, 32};
//+
Physical Line(2) = {27, 28};
//+
Physical Line(3) = {25, 26};
//+
Physical Line(4) = {30, 29};
//+
Physical Line(10) = {19, 20, 21, 22, 23, 24, 17, 18};
//+
Physical Surface(1) = {3, 4, 5, 6, 7, 8, 1, 2};
// 
// Add interior interfaces y=0, x=0, y=x and y=-x
//+
Physical Line(100) = {13, 9};
//+
Physical Line(101) = {15, 11};
//+
Physical Line(102) = {14, 10};
//+
Physical Line(103) = {12, 16};

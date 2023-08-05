DefineConstant[
N = {20, Name "Input/1Points "}
L = {100,  Name "Input/2L "}, // in millimeter
a = {5, Name "Input/3a"}, // in millimeter
R = {2.5,  Name "Input/4Radius "}, // in millimeter
l = {50,  Name "Input/5l "}, // in millimeter
b = {5,  Name "Input/6b "} // in millimeter
];

N=(N>=10 ? N : 10);
Mesh.Algorithm = 6;
Mesh.CharacteristicLengthMin = 10/N;
Mesh.CharacteristicLengthMax = 10/N;
h = 2/N;

Point(100) = {0, 0, 0, h};
Point(1) = {R, 0, 0, h};
Point(2) = {R+a, 0, 0, h};
Point(3) = {R, L, 0, h};
Point(4) = {R+a, L, 0, h};

Point(5) = {-R, 0, 0, h};
Point(6) = {-(R+a), 0, 0, h};
Point(7) = {-R, L, 0, h};
Point(8) = {-(R+a), L, 0, h};

Point(9) = {-b/2, -(R+a+l), 0, h};
Point(10) = {b/2, -(R+a+l), 0, h};


Point(20) = {0, -R, 0, h};
Point(21) = {-b/2,-Sqrt((R+a)*(R+a)-(b/2)*(b/2)), 0, h}; // A
Point(22) = { b/2,-Sqrt((R+a)*(R+a)-(b/2)*(b/2)), 0, h};  // B
//+
Line(1) = {2, 4};
//+
Line(2) = {4, 3};
//+
Line(3) = {3, 1};
//+
Line(4) = {1, 2};
//+
Line(5) = {5, 7};
//+
Line(6) = {7, 8};
//+
Line(7) = {8, 6};
//+
Line(8) = {6, 5};
//+
Line(9) = {9, 10};
//+
Line(10) = {22, 22};
//+
Line(11) = {10, 22};
//+
Line(12) = {22, 21};
//+
Line(13) = {21, 9};
//+
Circle(14) = {5, 100, 20};
//+
Circle(15) = {20, 100, 1};
//+
Circle(16) = {6, 100, 21};
//+
Circle(17) = {22, 100, 2};
//+
Line Loop(1) = {5, 6, 7, 16, 13, 9, 11, 17, 1, 2, 3, -15, -14};
//+
Plane Surface(1) = {1};
//+
Physical Line(1) = {9};
//+
Physical Line(2) = {11, 13};
//+
Physical Line(3) = {6, 7, 16, 17, 1, 2, 3, 5, 14, 15};
//+
Physical Surface(1) = {1};

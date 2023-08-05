DefineConstant[
N = {20, Name "Input/1Points "}
// L = {1,  Name "Input/2Rect "},
// r = {0.1, Name "Input/3Radius"}
];

N=(N>=10 ? N : 10);
Mesh.Algorithm = 6;
Mesh.CharacteristicLengthMin = 10/N;
Mesh.CharacteristicLengthMax = 10/N;

//+
Point(1) = {0, 0, 0, 1.0};
Point(2) = {0, 0, -2, 1.0};
Point(3) = {2, 0, 0, 1.0};
Point(4) = {-2, 0, 0, 1.0};
Point(5) = {2, 0, 18, 1.0};
Point(6) = {-2, 0, 18, 1.0};
Point(7) = {9, 0, 18, 1.0};
Point(8) = {-9, 0, 18, 1.0};
Point(9) = {8, 0, -19, 1.0};
Point(10) = {-9, 0, -19, 1.0};

Point(20) = {-4, 0, -8, 1.0};
Point(21) = {-4, 0, -10, 1.0};
Point(22) = {-4, 0, -14, 1.0};
Point(23) = {-4, 0, -16, 1.0};
Point(24) = {-6, 0, -10, 1.0};
Point(25) = {-6, 0, -14, 1.0};
Point(26) = {-2, 0, -10, 1.0};
Point(27) = {-2, 0, -14, 1.0};

Point(30) = {4, 0, -8, 1.0};
Point(31) = {4, 0, -10, 1.0};
Point(32) = {4, 0, -14, 1.0};
Point(33) = {4, 0, -16, 1.0};
Point(34) = {6, 0, -10, 1.0};
Point(35) = {6, 0, -14, 1.0};
Point(36) = {2, 0, -10, 1.0};
Point(37) = {2, 0, -14, 1.0};
//+
Circle(1) = {20, 21, 24};
//+
Circle(2) = {20, 21, 26};
//+
Circle(3) = {25, 22, 23};
//+
Circle(4) = {23, 22, 27};
//+
Circle(5) = {36, 31, 30};
//+
Circle(6) = {30, 31, 34};
//+
Circle(7) = {37, 32, 33};
//+
Circle(8) = {33, 32, 35};
//+
Circle(9) = {4, 1, 2};
//+
Circle(10) = {2, 1, 3};
//+
Line(11) = {10, 9};
//+
Line(12) = {9, 7};
//+
Line(13) = {7, 5};
//+
Line(14) = {5, 3};
//+
Line(15) = {4, 6};
//+
Line(16) = {6, 8};
//+
Line(17) = {8, 10};
//+
Line(18) = {24, 25};
//+
Line(19) = {26, 27};
//+
Line(20) = {36, 37};
//+
Line(21) = {34, 35};
//+
Line Loop(1) = {17, 11, 12, 13, 14, -10, -9, 15, 16};
//+
Line Loop(2) = {2, 19, -4, -3, -18, -1};
//+
Line Loop(3) = {20, 7, 8, -21, -6, -5};
//+
Plane Surface(1) = {1, 2, 3};
//+
Physical Line(1) = {11};
//+
Translate {0, 2, 0} {
  Duplicata { Surface{1}; }
}
//+
Line(44) = {7, 47};
//+
Line(45) = {5, 51};
//+
Line(46) = {2, 60};
//+
Line(47) = {55, 3};
//+
Line(48) = {4, 65};
//+
Line(49) = {6, 69};
//+
Line(50) = {38, 8};
//+
Line(51) = {10, 39};
//+
Line(52) = {9, 43};
//+
Line(53) = {33, 120};
//+
Line(54) = {115, 35};
//+
Line(55) = {37, 125};
//+
Line(56) = {34, 111};
//+
Line(57) = {30, 106};
//+
Line(58) = {36, 104};
//+
Line(59) = {23, 87};
//+
Line(60) = {25, 82};
//+
Line(61) = {27, 92};
//+
Line(62) = {26, 96};
//+
Line(63) = {24, 78};
//+
Line(64) = {20, 76};
//+
Line Loop(4) = {25, -44, -12, 52};
//+
Plane Surface(23) = {4};
//+
Line Loop(5) = {13, 45, -26, -44};
//+
Plane Surface(24) = {5};
//+
Line Loop(6) = {49, 31, 50, -16};
//+
Plane Surface(25) = {6};
//+
Line Loop(7) = {45, 27, 47, -14};
//+
Plane Surface(26) = {7};
//+
//+
Line Loop(10) = {48, 30, -49, -15};
//+
Plane Surface(29) = {10};
//+
Line Loop(11) = {50, 17, 51, -23};
//+
Plane Surface(30) = {11};
//+
Line Loop(12) = {11, 52, -24, -51};
//+
Plane Surface(31) = {12};
//+
Line Loop(13) = {40, 54, -21, 56};
//+
Plane Surface(32) = {13};
//+
//+
//+
//+
Line Loop(17) = {43, -58, 20, 55};
//+
Plane Surface(36) = {17};
//+
Line Loop(18) = {5, 57, -38, -58};
//+
Plane Surface(37) = {18};
//+
Line Loop(20) = {36, -62, 19, 61};
//+
Plane Surface(40) = {20};
//+
Line Loop(21) = {61, -35, -59, 4};
//+
Plane Surface(41) = {21};
//+
Line Loop(23) = {18, 60, -33, -63};
//+
Plane Surface(43) = {23};
//+//+
Line Loop(24) = {1, 63, -32, -64};
//+
Surface(44) = {24};
//+
Line Loop(25) = {34, -59, -3, 60};
//+
Surface(45) = {25};
//+
Surface(46) = {21};
//+
Line Loop(26) = {62, 37, -64, 2};
//+
Surface(47) = {26};
//+
Surface(48) = {18};
//+
Line Loop(27) = {6, 56, -39, -57};
//+
Surface(49) = {27};
//+
Line Loop(28) = {54, -8, 53, -41};
//+
Surface(50) = {28};
//+
Line Loop(29) = {7, 53, 42, -55};
//+
Surface(51) = {29};
//+
Line Loop(30) = {47, -10, 46, -28};
//+
Surface(52) = {30};
//+
Line Loop(31) = {29, -48, 9, 46};
//+
Surface(53) = {31};
//+
Surface Loop(1) = {1, 30, 25, 29, 53, 22, 31, 23, 24, 26, 52, 44, 43, 45, 47, 40, 49, 32, 50, 51, 36, 48, 46};
//+
Volume(1) = {1};
//+
Physical Surface(2) = {44, 47, 40, 46, 45, 43};
//+
Physical Surface(3) = {48, 49, 32, 50, 51, 36};
//+
Physical Surface(4) = {29, 53, 52, 26};
//+
Physical Surface(5) = {25, 24};
//+
Physical Surface(6) = {30};
//+
Physical Surface(7) = {23};
//+
Physical Surface(8) = {1};
//+
Physical Surface(9) = {22};
//+
Physical Surface(1) = {31};
//+
Physical Volume(1) = {1};

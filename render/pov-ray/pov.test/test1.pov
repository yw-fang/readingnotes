#include "colors.inc"
#include "stones.inc"

background {color Cyan}
camera{
location <0, 2, -3>
look_at <0, 1, 2>
}

sphere {
<0, 1, 2>, 1
//center of sphere, raidus
texture {
pigment {color Yellow}
}
}

//box{
// <-1,0,-1>
// <1,0.5,3>
// texture{
//  T_Stone25
//  scale 4
// }   
// rotate y*20
//}  

//cone{
// <0,1,-1>, 0.3
// <1,2,2>, 1.0
// texture {
// T_Stone25 scale 4
// }
//}             

cylinder{
 <0, 3, 2>
 <0, -1, 2>
 0.4
 open                                                
 texture {T_Stone25 scale 4}
} 

plane { <0, 1, 0>, -1
pigment {
checker color Red, color Blue
}
}

light_source {<2, 20, -3> color White}
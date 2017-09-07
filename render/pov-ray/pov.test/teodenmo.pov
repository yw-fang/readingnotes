#include "colors.inc"
camera {
  location <0, .1, -34>     
//  location <0, .1, -30>
  look_at <3., 0, 0>      
// look_at <0, 0, 0>
  angle 30
}         

background {color White} // to make the rorus easy to see
light_source {<300, 300, -1000> White}

#declare Half_Torus = difference{
torus{   
 4, 1
 rotate -90*x
   
 } 
  box {<-5, -5, -1>,<5, 0, 1>}    
   pigment {Yellow} 
 }

 
  #declare Flip_It_Over = 180*x;
 #declare Torus_Translate = 8;    //double major radius
 
// union {
//  object { Half_Torus }
//  object { Half_Torus 
//    rotate Flip_It_Over  
//    translate Torus_Translate*x  
//    translate Torus_Translate*<0,0.5,0>      
//  }
// }

union {
object { Half_Torus }
object { Half_Torus      
rotate Flip_It_Over
translate x*Torus_Translate
}   
object { Half_Torus      
//rotate Flip_It_Over
translate x*Torus_Translate*2
}  

object { Half_Torus      
rotate Flip_It_Over
translate x*Torus_Translate*3
} 

object { Half_Torus      
rotate Flip_It_Over
translate -x*Torus_Translate
}

object { Half_Torus      
//rotate Flip_It_Over
translate -x*Torus_Translate*2
}

object { Half_Torus
rotate Flip_It_Over
translate -x*Torus_Translate*3
}
object { Half_Torus
translate -x*Torus_Translate*4
}

rotate y*65  
translate z*30
}     

 

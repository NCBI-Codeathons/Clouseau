#include<string>
#include <map>

#include "Chr.h"

Chr::Chr(std::string chr_name, int position){
  SetChr(chr_name, position)
}

void SetChr(std::string chr_name, int position){
  this -> chr_name = chr_name;
  this -> start = position;
  this -> end = position;
}

void updatePosition(int position, int gap){

  if((postion - this->end) > gap)
    ; // for future this needs to be reported in log file.
  if(this->start > position){
    this->start = position;
  } else if (this->end > position){
    this->end = position;
  }
}

void addVariant(std::string variant){
  this->variants[varinat] ++;
}

#include "parsers.h"

void pileup_parse(int nucleot_list[4], int strand_list[4], char* pileup, char* quality, int depth, char reference, int qlimit, int noend, int nostart)
{
   char characters[] = "ACGTacgt$*Nn-+";

   char rev_reference;
   int n, q, last_base, offset, indel, step;
   n         = 0;
   q         = 0;
   last_base = -1;

   rev_reference = tolower(reference);

   while(pileup[n] != '\0') {
      char base = pileup[n];
      if (base == '^') {
         if (nostart == 0) {
            n += 2;
            base = pileup[n];
         } else {
            n += 3;
            q += 1;
            continue;
         }
      }
      if (base == '.') {
         base = reference;
      } else if( base == ',') {
         base = rev_reference;
      }
      int index = strchr(characters, base) - characters;
      int qual = quality[q];
      if (index < 4){
         if (qual >= qlimit) {
            last_base = index;
            nucleot_list[index] += 1;
            strand_list[index]  += 1;
         } else {
            last_base = -1;
         }
         n += 1;
         q += 1;
      } else if (index < 8) {
         if (qual >= qlimit) {
            last_base = index;
            nucleot_list[index - 4] += 1;
         } else {
            last_base = -1;
         }
         n += 1;
         q += 1;
      } else if (index == 8) {
         if (noend == 1) {
            if (last_base > -1) {
               if (last_base < 4) {
                  nucleot_list[last_base] -= 1;
                  strand_list[last_base]  -= 1;
               } else {
                  nucleot_list[last_base - 4] -= 1;
               }
            }
         }
         last_base = -1;
         n += 1;
      } else if (index >= 9 && index <= 11) {
         last_base = -1;
         n += 1;
         q += 1;
      } else if (index > 11) {
         offset = n + 1;
         indel = 0;
         for(;;) {
            if (isdigit(pileup[offset])) {
               if (indel == 0) {
                  step = pileup[offset] - '0';
               } else {
                  step = (step * 10) + (int)(pileup[offset] - '0');
               }
               indel += 1;
               offset += 1;
            } else {
               break;
            }
         }
         n = step + offset;
         indel = 0;
      }
   }
}

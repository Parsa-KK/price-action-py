



# this is an application that asks you the price action context and situations , and calculates different senarios and tells you how much risk is involved to enter a trade
# or how much chances are to succeed the trade and finally tells you to enter a trade or not



#variables111




#print (type(impulsiveelements));





#Senario = input("choose the existing senario :\n1.breakout\n2.fals-break\n3.20EMA\n4.3p HL\n5.RRL\n6.LS zone\n7.LLT\n8.Exhaustion\n9.advanced break entry\n");



############################################################## type of trends (impulsive vs corrective / volatile & non-volatile) ###############################################################

import math    

from statistics import variance

from fractions import Fraction as fr


totalLLTScore = 5.8;

totalLSzoneScore = 10;

totalRRLscore = 10;



#######################################################################  S/R ZONE Situations  ######################################################################################




def zone() :

            ##############################################################################################################   Zone Formation :

            #### this should be a part of a senario


            #######################################################################   LLT (S/R level limit level trades)

            zoneFormation = input("select zone formation : \n1.LLt\n2.LS zone\n3.RRL\n");

            if zoneFormation == "1" :






                totalLLTScore = 5.8;

                LLTscore = 0;

                LLTx2 = 0.2
                LLTx7 = 0.7 
                #LLTx3 = 4
                #LLTx2 = 2




                #LLt conditions
    
                WT = input("is it with trend?\n1.yes\n2.no\n");

                if WT == "1" :

                    
                    LLTscore += 1+(1*LLTx2);


    
                if WT == "2" :

                    LLTscore -= 1+(1*LLTx2);




                HT = input("is it supported by a higher time frame context?\n1.yes\n2.no\n");
    

                if HT == "1" :

                    LLTscore += 1+(1*LLTx2);


                if HT == "2" :

                    LLTscore -= 1+(1*LLTx2);




                respect = input("is it an well respected level?\n1.yes\n2.no\n");

                if respect == "1" :

                    LLTscore += 1+(1*LLTx7);


                if respect == "2" :
        
                    LLTscore -= 1+(1*LLTx7);
                    







                reaction = input("has it a srong reaction?\n1.yes\n2.no\n");
    
                if reaction == "1" :

                    LLTscore += 1+(1*LLTx7);


                if reaction == "2" :

                    LLTscore -= 1+(1*LLTx7);







                if LLTscore > 2 :


                    print("conditions are qualified for LLT");
                    print("Total LLT score is :" + str(totalLLTScore));
                    print("the LLT score is :" + str(LLTscore));


                    LLTweightedAvg = LLTscore/4
                    print("weighted average of LLT is : % s " %LLTweightedAvg)



                    # SPP : qualification percentage
                    def SPP (values) :


                        mainValue = (values/totalLLTScore)*100;

                        return mainValue;

                    finalResult = SPP(LLTscore);


                    if finalResult > 50.0 :
                                
                                
                                print("the percentage of qualification for LLT is : " + str(finalResult) + "%" );

                                # return to the zone func
                                return float(LLTscore) , "LLT" ;                                

                        

                    if finalResult < 50.0 :

                                print("the percentage of qualification for LLT is : " + str(finalResult) + "%" );

                                
                                return float(LLTscore) , "LLT" ;
            





            

                if LLTscore < 2 :
                        
                        exit();







            ############################################################################     weight of each condition must be considered    ############################################
        

            ####################################################################### LS Zone



            #definitions : as long as the price is above the LS zone we are bullish & as long as it's below the level we are bearish could be either in ranges or trends

            if zoneFormation == "2" :
        



                LSzoneType = input("determine LS zone Type : \n1.structure\n2.key swing point\n3.Long Term S/R Zone\n" );


                #structure

                if LSzoneType == "1" :


                    totalstructureScore = 5;

                    structureScore = 1;


                    # types of structure in LS zone

                    TypeStructure = input("choose the type of structure :\n1.larg consolidation range( Larg corrective structure balancing zone)\n2.breakout formation\n3.short term corrective structure failing break");

                    if TypeStructure == "1" :

                        LCR = 1;
                        ###needs codes
        
                    if TypeStructure == "2" :

                        BF = 1;
                        ###needs codes

                    if TypeStructure == "3" :

                        STCSF = 1;
                        ###needs codes












                # KSP definition :these are major swing point which have held trend in place oether allow them to continue or avoid them to continuing

                # they can also be swings that have created major new Leg in an already existing trend /they can be a part of an existing range
                if LSzoneType == "2" :



                    KSPscore = 1;

                    touches = input("number of touches represents : \n1.one\n2.two\n3.three");


                    if touches == "1" :

                            totalKSP1Tscore = 2;
                            KSPscore += 1;



                            FBsituation = input("is there any fals break appear?\n1.yes\n2.no\n");

                            if FBsituation == "1" & KSPscore >= 2 :
                






                                                print("conditions are qualified for KSP 1T");
                                                #functional programming
                                                print("the breakout score is :" + str(KSPscore));

                                                # SPP : success probability percentage
                                                def SPP (values) :


                                                    mainValue = (values/totalKSP1Tscore)*100;
                                        
                                                    return mainValue;

                                                finalResult = SPP(KSPscore);

                                                if finalResult > 80.0 :



                                                        #entry location

                                                        side = input("is it a fals break in a bullish context or a bearish context?\n1.bullish context\n2.bearish context\n");

                                                        if side == "1" :

                                                                print("fals break's high is a Key Swing Point if the bull make the price over this point , change your bias to Buy");


                                                        if side == "2" :

                                                                print("fals break's low is a Key Swing Point if the bears make the price below this point , change your bias to sell");



                                                if finalResult < 80.0 :

                                                            print("the percentage of success probabilty is : " + str(finalResult) );
                                                            print("the percentage of success probability is not qualified !!");


                                                #end of functional programming
                                                exit();      
                                    




                            
                            if FBsituation == "2" :


                                print("conditions are not qualified for KSP 1T");
                                exit();

















        
        


                    if touches == "2" :


                            totalKSP2Tscore = 2;
                            KSPscore += 1;


                            FBsituation = input("is there any fals break appear?\n1.yes\n2.no\n");

                            if FBsituation == "1" & KSPscore >= 2 :

                                                print("conditions are qualified for KSP 2T");
                                                #functional programming
                                                print("the breakout score is :" + str(KSPscore));

                                                # SPP : success probability percentage
                                                def SPP (values) :


                                                    mainValue = (values/totalKSP2Tscore)*100;
                                        
                                                    return mainValue;

                                                finalResult = SPP(KSPscore);

                                                if finalResult > 80.0 :



                                                        #entry location

                                                        side = input("is it a fals break in a bullish context or a bearish context?\n1.bullish context\n2.bearish context\n");

                                                        if side == "1" :

                                                                print("fals break's high is a Key Swing Point if the bull make the price over this point , change your bias to Buy");


                                                        if side == "2" :

                                                                print("fals break's low is a Key Swing Point if the bears make the price below this point , change your bias to sell");



                                                if finalResult < 80.0 :

                                                            print("the percentage of success probabilty is : " + str(finalResult) );
                                                            print("the percentage of success probability is not qualified !!");


                                                #end of functional programming
                                                exit();
                
                            
                            
                            if FBsituation == "2" :

                                print("conditions are not qualified for KSP 2T");
                                exit();

















                    if touches == "3" :
                

                            totalKSP3Tscore = 2;
                            KSPscore -= 1;

                            if KSPscore < 2 :



                                                print("conditions are not qualified for KSP 3T");
                                                #functional programming
                                                print("the KSPt score is :" + str(KSPscore));

                                                # SPP : success probability percentage
                                                def SPP (values) :


                                                    mainValue = (values/totalKSP3Tscore)*100;
                                        
                                                    return mainValue;

                                                finalResult = SPP(KSPscore);

                                                if finalResult < 80.0 :

                                                            print("the percentage of success probabilty is : " + str(finalResult) );
                                                            print("the percentage of success probability is not qualified !!");

                                                            print("conditions for KSP faild(when it has 3 touches we are talking about a long term S/R zone)");
                                                            #shift to long term S/R zone



                                                #end of functional programming
                                                            exit();













                # LTZ definition : are a part of a long term ranges(daily,weekly chart)
                # they are a mix of all the three types of the structure form
                # and they (can) also include KSP
                #
                if LSzoneType == "3" :


                    totalLTZscore = 5;
                    LTZscore = 1;

                    numberOfTouches = input("number of touches?\n1.one2.two\n3.three and more\n");
        
        
                    if numberOfTouches == "1" :

                        LTZscore -= 1;

                    if numberOfTouches == "2" :

                        LTZscore += 1;

                    if numberOfTouches == "3" :

                        LTZscore += 1;


                    if LTZscore >= 3 :

                                                print("conditions are qualified for LTZ");
                                                #functional programming
                                                print("the LTZ score is :" + str(LTZscore));

                                                # SPP : success probability percentage
                                                def SPP (values) :


                                                    mainValue = (values/totalLTZscore)*100;
                                        
                                                    return mainValue;

                                                finalResult = SPP(LTZscore);

                                                if finalResult > 80.0 :

                                                            print("the percentage of success probabilty is : " + str(finalResult) );
                                                            print("the percentage of success probability is qualified !!");


                                                #end of functional programming
                                                            exit();


                                                if finalResult < 80.0 :

                                                            print("the percentage of success probabilty is : " + str(finalResult) );
                                                            print("the percentage of success probability is not qualified !!");

                                                            print("conditions for KSP faild(when it has 3 touches we are talking about a long term S/R zone)");
                                                            #shift to long term S/R zone



                                                #end of functional programming
                                                            exit();

            if zoneFormation == "3" :

                totalRRLscore = 9;
                RRLscore = 0;

                ##### RRL
                # conditions :
                # with-trend / counter-trend
                # breakout senario :
                #                     all the pre-breakout conditions

                # several touches more stronger response
                #entry points



    
                breaking = input("do you see a level broken?\n1.yes\n2.no\n");

                if breaking == "1" :





                                    direction = input("is it during a with-trend or counter-trend situation?\n1.WT\n2.CT\n");

                                    if direction == "1" :


                                                            RRLscore += 1;

                                                            Tcon = input("are you in a with-trend situation or counter-trend situation?\n1.WT\n2.CT\n"); # not nessesary


                                                            if Tcon == "1" :

                                                                RRLscore += 1;
                                                                print("WT");
            


                                                            elif Tcon == "2" :

                                                                RRLscore -= 2;
                                                                print("CT");




                                                            volatility = input("is it during a non-volatile trend\n1.yes\n2.no");

                                                            if volatility == "1" :

                                                                        RRLscore += 1;

                                                            if volatility == "2" :

                                                                        RRLscore -= 1;

                            



                                                            touch = input("does is have the minimum of three touches?\n1.yes\n2.no\n");

                                                            if touch == "1" :

                                                                        RRLscore += 1;

                                                            if touch == "2" :

                                                                        RRLscore -= 1;




                                                            enviroment = input("is it a tight and constricted enviroment?\.1.yes\n2.no\n");
                
                                                            if enviroment == "1" :

                                                                    RRLscore += 1;

                                                            if enviroment == "2" :

                                                                    RRLscore -= 1;





                                                            timing = input("is the holding time of this level high?\.1.yes\n2.no\n");

                                                            if timing == "1" :

                                                                    RRLscore += 1;

                                                            if timing == "2" :

                                                                    RRLscore = RRLscore

                                                            ############################## needs check




                                                            weakness = input("do you see weaker rejections off the level each time?\n1.yes\n2.no\n");


                                                            if weakness == "1" :

                                                                        RRLscore += 1;

                                                            if weakness == "2" :

                                                                        RRLscore -= 1;


                                                            squeeze = input("do you see the squeeze at the probable breaking level\n1.yes\n2.no\n");

                                                            if squeeze == "1" :

                                                                            RRLscore += 1;


                                                            if squeeze == "2" :


                                                                            RRLscore -= 1;



                                                            EMA20hold = input("do you see that 20EMA holding long the way?\n1.yes\n2.no\n");

                                                            if EMA20hold == "1" :

                                                                        RRLscore += 1;

                                                            if EMA20hold == "2" :

                                                                        RRLscore -= 1;

 
                                        







                                                            if RRLscore >= 6 :
                                                                                                    


                                                                                print("conditions are qualified for RRL");
                                                                                #functional programming
                                                                                print("the RRL score is :" + str(RRLscore));

                                                                                # SPP : success probability percentage
                                                                                def SPP (values) :


                                                                                    mainValue = (values/totalRRLscore)*100;

                                                                                    return mainValue;

                                                                                finalResult = SPP(RRLscore);


                                                                                if finalResult > 66.0 :

                                                                                        print("you are qualified for RRL");
                                                                                        print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                        print("enter on the Level");
                                                                                        exit();


                                                                                if finalResult < 66.0 :

                                                                                            print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                            print("the percentage of success probability is not qualified !!");
                                                                                            exit();


                                                                                #end of functional programming





                                                            if RRLscore < 6 :



                                                                                print("conditions are not qualified for RRL");
                                                                                exit();




                if breaking == "2" :

                    RRLscore -= 1;
                    exit();





############## call function





































trend = input("insert type of trend.\n1.impulsive & corrective\n2.volatile trend\n3.non volatile trend\n");







###################################################################################### impulsive move

if trend == "1" :

       # impulsive & corrective

        print("impulsive condotions :\n\n");

       #Context = input("insert context.\n1.impulsive\n2.corrective\n")
        
        

       #if Context == "1" :


        impulsiveRate = 0;



        close = input("less presents of weaks and shadows?\n1.yes\n2.no\n");


        if close == "1" :
    
            impulsiveRate += 1;
        
        elif close == "2" :

            impulsiveRate = impulsiveRate;


        sameColors = input("at least 3 same color candles?\n1.yes\n2.no\n");


        if sameColors == "1" :

            impulsiveRate += 1;
        
        elif close == "2" :

            impulsiveRate = impulsiveRate;


        candleSize = input("big candles?\n1.yes\n2.no\n");
    
        if candleSize == "1" :

            impulsiveRate += 1;

        elif close == "2" :

            impulsiveRate = impulsiveRate;



        #final condition in impulsive elements section :

        if impulsiveRate >= 3 :

######################################################################################## corrective move conditions

                    print("conditions are exactly qualified for impulsive move\n\n");
                    print("corrective conditions :\n\n");


                    correctiveRate = 0;

            


                    close = input("more presents of weaks and shadows?\n1.yes\n2.no\n");


                    if close == "1" :
    
                            correctiveRate += 1;
        
                    elif close == "2" :
                
                            correctiveRate = correctiveRate;


                    mixcolors = input("1.mix color candles?\n");


                    if mixcolors == "1" :

                            correctiveRate += 1;
        
                    elif mixcolors == "2" :

                            correctiveRate = correctiveRate;


                    candleSize = input("1.small candles?\n");
    
                    if candleSize == "1" :

                            correctiveRate += 1;

                    elif candleSize == "2" :

                            correctiveRate = correctiveRate;






                    #final condition in corrective elements section
                    if correctiveRate >= 3 :

                                            ### Senario to enter

                                            print("conditions are exactly qualified for corrective move");
                                            print("conditions are exactly qualified for impulsive & corrective move");

                                            Senario = input("choose the existing senario :\n1.breakout\n2.fals-break\n3.20EMA\n4.3p HL\n5.RRL\n6.LS zone\n7.LLT\n8.Exhaustion\n9.advanced break entry\n");


#######################################################################  Breakout Senario  ############################################################################################################

                                            if Senario == "1" :

                                                                
                                                                breakoutScore = 0;
                                                                totalWTBreakoutScore = 10;
                                                                totalCTBreakoutScore = 3;

                                                                TypeOfEnviroment = input("determine enviroment type?\n1.trend\n2.range\n");




                                                                # trend inviroment 

                                                                if TypeOfEnviroment == "1" :

                                                                        
                                                                       
                                                                        breakoutScore += 1;



        
                                                                        trendExp = input("is the trend expired?\n1.yes\n2.no\n");

                                                                        if trendExp == "1" :

                                                                                breakoutScore -= 1;
                                                                                #exit();


                                                                        if trendExp == "2" :

                                                                                breakoutScore += 1;




                                                                                dir = input("is the possible breaking zone with trend or counter trend?\n1.With Trend\n2.Counter Trend\n");
    
                                                                                if dir == "1" :

                                                                                        breakoutScore += 1;

                                                                                        volatility = input("is it during a non-volatile trend\n1.yes\n2.no");

                                                                                        if volatility == "1" :

                                                                                                    breakoutScore += 1;

                                                                                        if volatility == "2" :

                                                                                                    breakoutScore -= 1;

                            



                                                                                        touch = input("does is have the minimum of two touches?\n1.yes\n2.no\n");

                                                                                        if touch == "1" :

                                                                                                    breakoutScore += 1;

                                                                                        if touch == "2" :

                                                                                                    breakoutScore -= 1;




                                                                                        enviroment = input("is it a tight and constricted enviroment?\.1.yes\n2.no\n");
                
                                                                                        if enviroment == "1" :

                                                                                                breakoutScore += 1;

                                                                                        if enviroment == "2" :

                                                                                                breakoutScore -= 1;





                                                                                        timing = input("is the holding time of this level high?\.1.yes\n2.no\n");

                                                                                        if timing == "1" :

                                                                                                breakoutScore += 1;

                                                                                        if timing == "2" :

                                                                                                breakoutScore = breakoutScore;

                                                                                        ############################## needs check




                                                                                        weakness = input("do you see weaker rejections off the level each time?\n1.yes\n2.no\n");


                                                                                        if weakness == "1" :

                                                                                                    breakoutScore += 1;

                                                                                        if weakness == "2" :

                                                                                                    breakoutScore -= 1;


                                                                                        squeeze = input("do you see the squeeze at the probable breaking level\n1.yes\n2.no\n");

                                                                                        if squeeze == "1" :

                                                                                                        breakoutScore += 1;


                                                                                        if squeeze == "2" :


                                                                                                        breakoutScore -= 1;



                                                                                        EMA20hold = input("do you see that 20EMA holding long the way?\n1.yes\n2.no\n");

                                                                                        if EMA20hold == "1" :

                                                                                                    breakoutScore += 1;

                                                                                        if EMA20hold == "2" :

                                                                                                    breakoutScore -= 1;

                            
                                                                                        if breakoutScore >= 10 :
                                                                                                    


                                                                                                print("conditions are qualified for WT breakout");
                                                                                                #functional programming
                                                                                                print("the breakout score is :" + str(breakoutScore));

                                                                                                # SPP : success probability percentage
                                                                                                def SPP (values) :


                                                                                                    mainValue = (values/totalWTBreakoutScore)*100;

                                                                                                    return mainValue;

                                                                                                finalResult = SPP(breakoutScore);


                                                                                                if finalResult < 80.0 :

                                                                                                            print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                                            print("the percentage of success probability is not qualified !!");


                                                                                                #end of functional programming
                                                                                                exit();



                                                                                        if breakoutScore < 10 :

                                                                                                print("conditions are not qualified for WT breakout");
                                                                                                exit();                                                                                                       
                                                                                        # needs more caculation












                                                                                        ##### 20EMA penetrations getting weaker (input)
                            


                                                                                        #### couple doji around the level (weighty condition)
                            


                                                                                        #if breakoutScore >= 3 :

                                                                                            #entry = input("");

                                                                                            #pre-breakout
                                                                                            #RRL
                                                                                            #20EMA
            
                                                                                        # total value and comparing to final rate to make a percentage











                                                                                #counter trend breakout

                                                                                if dir == "2" :

                                                                                        breakoutScore = 1;

                                                                                        CT = input("is there any counter trend in lower time frame inside of the main Counter Trend?\n1.yes\n2.no\n");
        

                                                                                        if CT == "1" :

                                                                                                breakoutScore += 1;



                                                                                                entry = input("do you see any of these following candles to enter? select if you do\n1.pinbar rejection\2.inside bar\n3.shave bar\n4.ingulfing bar\n5. 6nt pullback\n");

                                                                                                if entry == "1" | "2" | "3" | "4" | "5" :

                                                                                                        breakoutScore += 1;





                                                                                                if breakoutScore >= 3 :
                                                                                                    


                                                                                                        print("conditions are qualified for CT break out");
                                                                                                        #functional programming
                                                                                                        print("the breakout score is :" + str(breakoutScore));

                                                                                                        # SPP : success probability percentage
                                                                                                        def SPP (values) :


                                                                                                            mainValue = (values/totalCTBreakoutScore)*100;

                                                                                                            return mainValue;

                                                                                                        finalResult = SPP(breakoutScore);


                                                                                                        if finalResult < 80.0 :

                                                                                                                    print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                                                    print("the percentage of success probability is not qualified !!");


                                                                                                        #end of functional programming
                                                                                                        exit();



                                                                                                if breakoutScore < 3 :

                                                                                                        print("conditions are not qualified for CT break out");
                                                                                                        exit();


                                                                                        if CT == "2" :

                                                                                                breakoutScore -= 1;
                                                                                                exit();




                                                                # range inviroment
                                                                if TypeOfEnviroment == "2" :
        
                                                                        breakoutScore = breakoutScore;








#######################################################################  fals-Break Senario  #########################################################################################


                                            if Senario == "2" :

                                                totalKeyLevelWTFB = 7;
                                                totalKeyLevelCTFB = 7;
                                                totalStructuralWTFB = 7;
                                                totalStructuralCTFB = 7;


                                                FBscore = 0;
    
                                                category = input("determine the following categories :\n1.fals break in key Level/zone\n2.fals break in a structure(structural)\n");

                                                # fals-break in a key level/zone
                                                if category == "1" :



                                                        dir = input("select the existing direction :\n1.with trend\n2.counter trend\n");

                                                        
                                                        ################### with trend fals break (key level/zone)
                                                        if dir == "1" : 

                                                                FBscore += 1;

                                                                level = input("is there any key level that acted as a key S/R ?\n1.yes\n2.no\n");
                            

                                                                if level == "1" :

                                                                            FBscore += 1;

                                                                if level == "2" :

                                                                            FBscore -= 1;

                                                                breaking = input("is level got broken?\n1.yes\n2.no\n");
                    
                                                                if breaking == "1" :

                                                                            FBscore += 1;

                                                                if breaking == "2" :

                                                                            FBscore -= 1;


                                                                sideway = input("is price playing side ways without any aggressive move?\n1.yes\n2.no\n");

                                                                if sideway == "1" :

                                                                            FBscore +=1;

                                                                if sideway == "2" :

                                                                            FBscore -= 1;



                                                                present = input("is there more present of the with trend players with same candle colors ?\n1.yes\n2.no\n");

                                                                if present == "1" :

                                                                            FBscore += 1;

                                                                if present == "2" :

                                                                            FBscore -= 1;



                                                                cumulation = input("or even see a cumulation like HL or LH?\n1.yes\n2.no\n");

                                                                if cumulation == "1" :

                                                                            FBscore += 1;

                                                                if cumulation == "2" :

                                                                            FBscore -= 1;                                                                            



                                                                close == input("is the price closed back to the prior broken level?\n1.yes\n2.no\n");

                                                                if close == "1" :
                        
                                                                            FBscore += 1;

                                                                if close == "2" :


                                                                            FBscore -= 1;


                                                                ################ entry

                                                                if FBscore >= 5 :

                                                                            print("look for a pullback to the fals-broken level");
                                                                            print("the false break score is :" + str(FBscore));

                                                                            #functional programming


                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalKeyLevelWTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult > 80.0 :

                                                                                print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                print("the percentage of success probability is qualified !!");


                                                                            #end of functional programming
                                                                            exit();






                                                                elif FBscore < 5 :

                                                                            print("conditions for WT fals break senario are not qulified");
                                                                            #functional programming
                                                                            print("the false break score is :" + str(FBscore));

                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalKeyLevelWTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();







                                                        ################### counter trend fals break (key level/zone)
                                                        if dir == "2" :

                                                                FBscore += 1;

                                                                level = input("is there any key level that acted as a key S/R ?\n1.yes\n2.no\n");
                            

                                                                if level == "1" :

                                                                            FBscore += 1;

                                                                if level == "2" :

                                                                            FBscore -= 1;

                                                                breaking = input("is level got broken?\n1.yes\n2.no\n");
                    
                                                                if breaking == "1" :

                                                                            FBscore += 1;

                                                                if breaking == "2" :


                                                                            FBscore -= 1;


                                                                sideway = input("is price playing side ways without any aggressive move?\n1.yes\n2.no\n");

                                                                if sideway == "1" :

                                                                            FBscore +=1;

                                                                if sideway == "2" :

                                                                            FBscore -= 1;



                                                                present = input("is there more present of the counter trend players with same candle colors?\n1.yes\n2.no\n");

                                                                if present == "1" :

                                                                            FBscore +=1;

                                                                if present == "2" :

                                                                            FBscore -= 1;


                                                                cumulation = input("or even see a cumulation like HL or LH?\n1.yes\n2.no\n");

                                                                if cumulation == "1" :

                                                                            FBscore += 1;

                                                                if cumulation == "2" :

                                                                            FBscore -= 1;


                                                                close == input("is the price closed back to the prior broken level?\n1.yes\n2.no\n");

                                                                if close == "1" :
                        
                                                                            FBscore += 1;

                                                                if close == "2" :


                                                                            FBscore -= 1;


                                                                ################ entry

                                                                if FBscore >= 5 :

                                                                            print("look for a pullback to the fals-broken level");
                                                                            print("the false break score is :" + str(FBscore));
                                                                            #functional programming


                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalKeyLevelCTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();





                                                                elif FBscore < 5 :

                                                                            print("conditions for CT fals break senario are not qulified");
                                                                            print("the false break score is :" + str(FBscore));
                                                                            #functional programming


                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalKeyLevelCTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult));
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();


























                                                # fals-break in a structure(structural)
                                                if category == "2" :
         
                                                        
                                                        dir = input("select the existing direction :\n1.with trend\n2.counter trend\n");


                                                        ################### with trend fals break (structural)
                                                        if dir == "1" : 

                                                                FBscore += 1;

                                                                level = input("is there any key level of a structure that acted as a key S/R ?\n1.yes\n2.no\n");
                            

                                                                if level == "1" :

                                                                            FBscore += 1;

                                                                if level == "2" :

                                                                            FBscore -= 1;


                                                                touch = input("has it the minimum of two touches?\n1.yes\n2.no\n");


                                                                if touch == "1" : 

                                                                            FBscore += 1;
                    

                                                                if touch == "2" :


                                                                            FBscore -= 1;




                                                                breaking = input("is level got broken?\n1.yes\n2.no\n");
                    
                                                                if breaking == "1" :

                                                                            FBscore += 1;

                                                                if breaking == "2" :


                                                                            FBscore -= 1;


                                                                sideway = input("is price playing side ways without any aggressive move?\n1.yes\n2.no\n");

                                                                if sideway == "1" :

                                                                            FBscore +=1;

                                                                if sideway == "2" :

                                                                            FBscore -= 1;


                                                                present = input("is there more present of the with trend players with same candle colors?\n1.yes\n2.no\n");

                                                                if present == "1" :

                                                                            FBscore +=1;

                                                                if present == "2" :

                                                                            FBscore -= 1;


                                                                cumulation = input("or even see a cumulation like HL or LH?\n1.yes\n2.no\n");

                                                                if cumulation == "1" :

                                                                            FBscore +=1;

                                                                if cumulation == "2" :

                                                                            FBscore -= 1;


                                                                close == input("is the price closed back to the prior broken level?\n1.yes\n2.no\n");

                                                                if close == "1" :
                        
                                                                            FBscore += 1;

                                                                if close == "2" :


                                                                            FBscore -= 1;


                                                                ################ entry

                                                                if FBscore >= 6 :

                                                                            print("look for a pullback to the fals-broken level");

                                                                            print("the false break score is :" + str(FBscore));
                                                                            #functional programming


                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalStructuralWTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult));
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();



                                                                elif FBscore < 6 :

                                                                            print("conditions for fals break senario are not qulified");

                                                                            print("the false break score is :" + str(FBscore));
                                                                            #functional programming


                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalStructuralWTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult));
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();





                                                        ################### counter trend fals break (structural)
                                                        if dir == "2" :


                                                                FBscore += 1;

                                                                level = input("is there any key level of a structure that acted as a key S/R ?\n1.yes\n2.no\n");
                            

                                                                if level == "1" :

                                                                            FBscore += 1;

                                                                if level == "2" :

                                                                            FBscore -= 1;



                                                                touch = input("has it the minimum of two touches?\n1.yes\n2.no\n");


                                                                if touch == "1" : 

                                                                            FBscore += 1;
                    

                                                                if touch == "2" :


                                                                            FBscore -= 1;




                                                                breaking = input("is level got broken?\n1.yes\n2.no\n");
                    
                                                                if breaking == "1" :

                                                                            FBscore += 1;

                                                                if breaking == "2" :


                                                                            FBscore -= 1;


                                                                sideway = input("is price playing side ways without any aggressive move?\n1.yes\n2.no\n");

                                                                if sideway == "1" :

                                                                            FBscore +=1;

                                                                if sideway == "2" :

                                                                            FBscore -= 1;



                                                                present = input("is there more present of the counter trend players with same candle colors?\n1.yes\n2.no\n");

                                                                if present == "1" :

                                                                            FBscore +=1;

                                                                if present == "2" :

                                                                            FBscore -= 1;


                                                                cumulation = input("or even see a cumulation like HL or LH?\n1.yes\n2.no\n");

                                                                if cumulation == "1" :

                                                                            FBscore += 1;

                                                                if cumulation == "2" :

                                                                            FBscore -= 1;


                                                                close == input("is the price closed back to the prior broken level?\n1.yes\n2.no\n");

                                                                if close == "1" :
                        
                                                                            FBscore += 1;

                                                                if close == "2" :


                                                                            FBscore -= 1;

                    

                    

                                                                ################ entry

                                                                if FBscore >= 6 :

                                                                            print("look for a pullback to the fals-broken level");

                                                                            print("the false break score is :" + str(FBscore));
                                                                            #functional programming


                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalStructuralCTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult));
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();











                                                                elif FBscore < 6 :

                                                                            print("conditions for fals break senario are not qulified");

                                                                            print("the false break score is :" + str(FBscore));
                                                                            #functional programming


                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalStructuralCTFB)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(FBscore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult));
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();






                                                                            


                    elif correctiveRate < 3 : 
        
                                    print("conditions are not qualified for corrective move ");
                                    exit();











        elif impulsiveRate < 3 : 
        
            print("conditions are not qualified for impulsive move");
            exit();





 ###################################################################################### volatile trend  #########################################################################################


if trend == "2" :


        volatileRate = 1;
        totalVolatileRate = 6;

        #volatile trend conditions

        twentyEMA = input("1.playing both side of the 20EMA?\n");


        if twentyEMA == "1" :
    
            volatileRate += 1;
        



        wideChannel = input("1.moving in a wide channel?\n");


        if wideChannel == "1" :

            volatileRate += 1;
        



        greatCT = input("1.has a greater counter trend and pushbacks?\n");
    
        if greatCT == "1" :

            volatileRate += 1;




        levelOfImbalance = input("1.level of imbalace is not as that strong as it is in non-volatile type ?\n");
    
        if levelOfImbalance == "1" :

            volatileRate += 1;


        #final condition in volatile elements section
        if volatileRate >= 5 :

                #clean or un-clean volatile trend

                volatileType = input("1.clean\n2.un-clean\n");

                if volatileType == "1" :

                        cleanCon = input("are the prior level well respected?\n1.yes\n2.no\n");

                        if cleanCon == "1" :



                                volatileRate += 1;
                                print(volatileRate);



                                #####Entry_Point
                                # total value and comparing to final rate to make a percentage

                                if volatileRate >= 6 :

                                            #functional programming


                                            # SPP : success probability percentage
                                            def SPP (values) :


                                                mainValue = (values/totalVolatileRate)*100;

                                                return mainValue;

                                            finalResult = SPP(volatileRate);

                                            print("the percentage of success probabilty is : " + str(finalResult) );



                                            #end of functional programming











                                            Senario = input("entry points:\n\n1.pullback on prior S/R Level\n2.counter trend trade\n3.fals-break\n4.3p HL\n");

                                            if Senario == "1" :
                                                print("time to trade !!");


                                            if Senario == "2" :
                                                print("time to trade !!");
            
                                            if Senario == "3" :
                                                print("in volatile trend it's not time to trade breakouts because of no heay order flow in trade direction and more presents of the counter trend players");
                                                exit();

                                            ##########################   3P HL structure   
                                            if Senario == "4" :


                                                total3PScore = 6;
                                                threePointHigherLowScore = 0;


                                                con1 = input("is there any impulsive type move?\n1.yes\n2.no\n");


                                                if con1 == "1" :

                                                            threePointHigherLowScore +=1;


                                                if con1 == "2" :
        
                                                            threePointHigherLowScore -= 1;



                                                con2 = input("do you see any significant rejecetion after that impulsive move?\n1.yes\n2.no\n");


                                                if con2 == "1" :


                                                            threePointHigherLowScore += 1;

                                                            numberOfCandles = input("is number candles in this rejection somewhere between 3 - 15 or even 20? \n1.yes\n2.no\n");

                                                            if numberOfCandles == "1" :


                                                                        threePointHigherLowScore += 1;


                                                            if numberOfCandles == "2" :

                                                                        threePointHigherLowScore -= 1;

                                                if con2 == "2" :


                                                            threePointHigherLowScore -= 1;






                                                con3 = input("do you see a Lower Low?\n1.yes\n2.no\n");


                                                if con3 == "1" :


                                                            threePointHigherLowScore += 1;

                                                            LLcondition = input("is the price(the rejection of lower low) passed over the point that first swing rejection had a pullback to?\n1.yes\n2.no\n");
                
                                                            if LLcondition == "1" : 

                                                                        threePointHigherLowScore -= 1;
                                                                        # it shouldn't pass over
                                

                                                            if LLcondition == "2" :


                                                                        threePointHigherLowScore += 1;
 
                                                if con3 == "2" :


                                                            threePointHigherLowScore -= 1;


                                                con4 = input("do you see a Higher Low in relationship to the prior Lower Low?\n1.yes\n2.no\n");

                                                if con4 == "1" :


                                                            threePointHigherLowScore += 1;
                

                                                            numberOfCandles = input("has the move that created third point(higher low) , almost the same number of candles as the first point had(first rejection)?\n1.yes\n2.no\n");

                                                            if numberOfCandles == "1" :


                                                                        threePointHigherLowScore += 1;

                                                            if numberOfCandles == "2" :


                                                                        threePointHigherLowScore -= 1;


                


                                                if con4 == "2" :
        
                                                            threePointHigherLowScore -= 1;




                                                if threePointHigherLowScore >= 6  :

                                                            # entry conditions
                                                            
                                                             

                                                            print("conditions for 3P HL senario are qulified");

                                                            print("the 3P HL score is :" + str(threePointHigherLowScore));

                                                            print("Look for a pinbar rejection to enter");



                                                            #functional programming


                                                            # SPP : success probability percentage
                                                            def SPP (values) :


                                                                mainValue = (values/total3PScore)*100;

                                                                return mainValue;

                                                            finalResult = SPP(threePointHigherLowScore);


                                                            if finalResult < 80.0 :

                                                                        print("the percentage of success probabilty is : " + str(finalResult));
                                                                        print("the percentage of success probability is not qualified !!");


                                                            #end of functional programming
                                                            exit();
                                                            #######################################################################################




                                                elif threePointHigherLowScore < 6 :



                                                            print("conditions for 3P HL senario are not qulified");

                                                            print("the 3P HL score is :" + str(threePointHigherLowScore));

                                                            print("Look for a pinbar rejection to enter");



                                                            #functional programming


                                                            # SPP : success probability percentage
                                                            def SPP (values) :


                                                                mainValue = (values/total3PScore)*100;

                                                                return mainValue;

                                                            finalResult = SPP(threePointHigherLowScore);


                                                            if finalResult < 80.0 :

                                                                        print("the percentage of success probabilty is : " + str(finalResult));
                                                                        print("the percentage of success probability is not qualified !!");


                                                            #end of functional programming
                                                            exit();                                                            
                                                            




                                                #target

                                                #stop-loss

















                        if cleanCon == "2" :

                            print(volatileRate);
                            print("not qualified");
                            exit();







                if volatileType == "2" :

                        
                        volatileRate -= 1;

                        if volatileRate < 6 :

                            print(volatileRate);
                            
                            



                            #functional programming


                            # SPP : success probability percentage
                            def SPP (values) :


                                mainValue = (values/totalVolatileRate)*100;

                                return mainValue;

                            finalResult = SPP(volatileRate);

                            print("the percentage of success probabilty is : " + str(finalResult) );









                            if finalResult < 80.0 :

                                        print("take a step back / look at larger context / see if it's forming a channel or reacting to something you cann't see ");


                            #end of functional programming
                            exit();






        elif volatileRate < 5 :


                print(volatileRate);        
                print("conditions are not qualified for volatile trend ");
                exit();










    #################################################################################### non-volatile trend #######################################################################################

if trend == "3" :

        nonVolatileRate = 1;
        #nonVolatileX2 = 0.2; 
        totalNonVolatileRate = 5;        
        #print(rate);

        channels = input("1.moving in a very tight channel?\n");


        if channels == "1" :
    
            nonVolatileRate += 1;
        



        CTpullback = input("1.weak & small CT candles in trend?\n");


        if CTpullback == "1" :

            nonVolatileRate += 1;
        



        breakThrough = input("1.is it break through any counter resistance?\n");
    
        if breakThrough == "1" :

            nonVolatileRate += 1;




        nonVolTwentyEMA = input("1.less touch and less penetration of the 20EMA ?\n");
    
        if nonVolTwentyEMA == "1" :

            nonVolatileRate += 1;






        #final condition in non-volatile elements section
        if nonVolatileRate >= 2.5 :




                    #functional programming

                    # this section requires "if" condition in case of LLT senario

                    
                    #totalNonVolatileRate = 5;
                    




                    zone_score , types = zone()

                    if types == "LLT" : 


                                        print("zone score is :" + str(zone_score))

                                        print( "zone type is : " + types);

                                        totalscore = totalNonVolatileRate + totalLLTScore

                                        total_gained_score = nonVolatileRate + float(zone_score)





                                        # SPP : success probability percentage
                                        def SPP (values) :

                                            
                                            print("nonVolatile score is : " + str(nonVolatileRate))
                                            print("total gained score is : " + str(total_gained_score))
                                            print("Total score is : " + str(totalscore))
                                            mainValue = (values/totalscore)*100;

                                            return mainValue;

                                        finalResult = SPP(total_gained_score);

                                        print("the percentage of success probabilty is : " + str(finalResult) );
                    






                    if types == "LSzone" :
                                        
                            
                                        print("zone score is :" + str(zone_score))

                                        print( "zone type is : " + types);

                                        totalscore = totalNonVolatileRate + totalLSzoneScore

                                        total_gained_score = nonVolatileRate + float(zone_score)



                                        

                                        # SPP : success probability percentage
                                        def SPP (values) :

                                            
                                            print("nonVolatile score is : " + str(nonVolatileRate))
                                            print("total gained score is : " + str(total_gained_score))
                                            print("Total score is : " + str(totalscore))
                                            mainValue = (values/totalscore)*100;

                                            return mainValue;

                                        finalResult = SPP(total_gained_score);

                                        print("the percentage of success probabilty is : " + str(finalResult) );
                    






                    if types == "RRL" :




                                        print("zone score is :" + str(zone_score))

                                        print( "zone type is : " + types);

                                        totalscore = totalNonVolatileRate + totalRRLscore

                                        total_gained_score = nonVolatileRate + float(zone_score)




                                        # SPP : success probability percentage
                                        def SPP (values) :

                                            
                                            print("nonVolatile score is : " + str(nonVolatileRate))
                                            print("total gained score is : " + str(total_gained_score))
                                            print("Total score is : " + str(totalscore))
                                            mainValue = (values/totalscore)*100;

                                            return mainValue;

                                        finalResult = SPP(total_gained_score);

                                        print("the percentage of success probabilty is : " + str(finalResult) );

                    # Variance :

                    #vrns = (variance(total_gained_score))

                    #print("variance of total score is : % s" %vrns )


                    # standard deviation :

                    #final_sqrt = math.sqrt(vrns)

                    #print("the standard deviation is : % s" %final_sqrt)


                    # export :

                    #to_hundred = (final_sqrt*100)


                    #print ("after * 100 is : % s" %to_hundred)

                    #times_total_score = totalscore * 100
                    #export = (to_hundred/times_total_score) * 100


                    #print("export is : % s" %export) 

                    #end of functional programming

















                    ### Entery (non-volatile)
                    print("let's go!");

                    nonVolEnrtry = input("entry points:\n\n1.looking for a pullback\n2.looking for counter trend trade\n3.looking for a breakout");

                    if nonVolEnrtry == "1" :

                                    print("in non volatile trend is not time to look for entery on pullbacks");
                                    exit();

                    if nonVolEnrtry == "2" :

                                    print("in non volatile trend is not time to look for trading counter trends");
                                    exit();









                    if nonVolEnrtry == "3" :

                    
                                    print("let's go!");
                                    

                                    # breakout conditions

                                    breakoutScore = 0;
                                    totalWTBreakoutScore = 10;
                                    totalCTBreakoutScore = 3;

                                    TypeOfEnviroment = input("determine enviroment type?\n1.trend\n2.range\n");




                                    # trend inviroment 

                                    if TypeOfEnviroment == "1" :

                                                                        
                                                                       
                                            breakoutScore += 1;



        
                                            trendExp = input("is the trend expired?\n1.yes\n2.no\n");

                                            if trendExp == "1" :

                                                    breakoutScore -= 1;
                                                    #exit();


                                            if trendExp == "2" :

                                                    breakoutScore += 1;




                                                    dir = input("is the possible breaking zone with trend or counter trend?\n1.With Trend\n2.Counter Trend\n");
    
                                                    if dir == "1" :

                                                            breakoutScore += 1;

                                                            volatility = input("is it during a non-volatile trend\n1.yes\n2.no"); # not nessesary

                                                            if volatility == "1" :

                                                                        breakoutScore += 1;

                                                            if volatility == "2" :

                                                                        breakoutScore -= 1;

                                                            



                                                            touch = input("does is have the minimum of two touches?\n1.yes\n2.no\n");

                                                            if touch == "1" :

                                                                        breakoutScore += 1;

                                                            if touch == "2" :

                                                                        breakoutScore -= 1;




                                                            enviroment = input("is it a tight and constricted enviroment?\.1.yes\n2.no\n");
                
                                                            if enviroment == "1" :

                                                                    breakoutScore += 1;

                                                            if enviroment == "2" :

                                                                    breakoutScore -= 1;





                                                            timing = input("is the holding time of this level high?\.1.yes\n2.no\n");

                                                            if timing == "1" :

                                                                    breakoutScore += 1;

                                                            if timing == "2" :

                                                                    breakoutScore = breakoutScore;

                                                            ############################## needs check




                                                            weakness = input("do you see weaker rejections off the level each time?\n1.yes\n2.no\n");


                                                            if weakness == "1" :

                                                                        breakoutScore += 1;

                                                            if weakness == "2" :

                                                                        breakoutScore -= 1;


                                                            squeeze = input("do you see the squeeze at the probable breaking level\n1.yes\n2.no\n");

                                                            if squeeze == "1" :

                                                                            breakoutScore += 1;


                                                            if squeeze == "2" :


                                                                            breakoutScore -= 1;



                                                            EMA20hold = input("do you see that 20EMA holding long the way?\n1.yes\n2.no\n");

                                                            if EMA20hold == "1" :

                                                                        breakoutScore += 1;

                                                            if EMA20hold == "2" :

                                                                        breakoutScore -= 1;








                            
                                                            if breakoutScore >= 10 :
                                                                                                    


                                                                    print("conditions are qualified for WT breakout");
                                                                    #functional programming
                                                                    print("the breakout score is :" + str(breakoutScore));

                                                                    # SPP : success probability percentage
                                                                    def SPP (values) :


                                                                        mainValue = (values/totalWTBreakoutScore)*100;

                                                                        return mainValue;

                                                                    finalResult = SPP(breakoutScore);


                                                                    if finalResult < 80.0 :

                                                                                print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                print("the percentage of success probability is not qualified !!");


                                                                    #end of functional programming
                                                                    exit();








                                                            
                                                            

                                                            if breakoutScore < 10 :

                                                                    print("conditions are not qualified for WT breakout");
                                                                    exit();                                                                                                       
                                                            # needs more caculation












                                                            ##### 20EMA penetrations getting weaker (input)
                            


                                                            #### couple doji around the level (weighty condition)
                            


                                                            #if breakoutScore >= 3 :

                                                                #entry = input("");

                                                                #pre-breakout
                                                                #RRL
                                                                #20EMA
            
                                                            # total value and comparing to final rate to make a percentage











                                                    #counter trend breakout

                                                    if dir == "2" :

                                                            breakoutScore = 1;

                                                            CT = input("is there any counter trend in lower time frame inside of the main Counter Trend?\n1.yes\n2.no\n");
        

                                                            if CT == "1" :

                                                                    breakoutScore += 1;



                                                                    entry = input("do you see any of these following candles to enter? select if you do\n1.pinbar rejection\2.inside bar\n3.shave bar\n4.ingulfing bar\n5. 6nt pullback\n");

                                                                    if entry == "1" | "2" | "3" | "4" | "5" :

                                                                            breakoutScore += 1;





                                                                    if breakoutScore >= 3 :
                                                                                                    


                                                                            print("conditions are qualified for CT break out");
                                                                            #functional programming
                                                                            print("the breakout score is :" + str(breakoutScore));

                                                                            # SPP : success probability percentage
                                                                            def SPP (values) :


                                                                                mainValue = (values/totalCTBreakoutScore)*100;

                                                                                return mainValue;

                                                                            finalResult = SPP(breakoutScore);


                                                                            if finalResult < 80.0 :

                                                                                        print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                        print("the percentage of success probability is not qualified !!");


                                                                            #end of functional programming
                                                                            exit();



                                                                    if breakoutScore < 3 :

                                                                            print("conditions are not qualified for CT break out");
                                                                            exit();


                                                            if CT == "2" :

                                                                    breakoutScore -= 1;
                                                                    exit();




                                    # range inviroment
                                    if TypeOfEnviroment == "2" :
        
                                            breakoutScore = breakoutScore;







        elif nonVolatileRate < 5 : 
        
            print("conditions are not qualified for non-volatile trend ");
            exit();










#######################################################################  exhaustion Senario  #########################################################################################

def exhaustion () :
                        


                        if Senario == "8" :



                            totalLTExhaustionScore = 5;
                            ExhaustionScore = 0;



                            # every Exhaustion has a CT impulsive move away sharper than the impulsive move Up
                            # determine the term of trend
                            term = input("is it long term trend or an intra-day trend?\n1.long term(weekly/monthly chart)\n2.intra-day\n");


                            # long term type

                            if term == "1" :


                                # it has only with trend type
                                ExhaustionScore += 1;


                                context = input("is it with trend?\n1.yes\n2.no\n");

                                if context == "1" :

                                                        #with trend
                                                        #long term WT is the hardest

                                                        ExhaustionScore += 1;


                                                        keyCon1 = input("occur after several bars have?\n1.yes\n2.no\n");

                                
                                                        if keyCon1 == "1" :


                                                            ExhaustionScore += 1;


                                                        if keyCon1 == "2" :

                                                            ExhaustionScore -= 1;



                                                        keyCon2 = input("the largest bar in the series\n1.yes\n2.no\n");


                                                        if keyCon2 == "1" :


                                                            ExhaustionScore += 1;


                                                        if keyCon2 == "2" :

                                                            ExhaustionScore -= 1;


                                                        keyCon3 = input("occur near key support/resistance level or on the break of one\n1.yes\n2.no\n");
                                                


                                                        if keyCon3 == "1" :


                                                            ExhaustionScore += 1;


                                                        if keyCon3 == "2" :

                                                            ExhaustionScore -= 1;


                                    ######################################### entry
                                    
                                                        if ExhaustionScore >= 5 :
                                



                                                                                    print("conditions are qualified for Exhaustion");
                                                                                    #functional programming
                                                                                    print("the Exhaustion score is :" + str(ExhaustionScore));

                                                                                    # SPP : success probability percentage
                                                                                    def SPP (values) :


                                                                                        mainValue = (values/totalLTExhaustionScore)*100;

                                                                                        return mainValue;

                                                                                    finalResult = SPP(ExhaustionScore);


                                                                                    if finalResult > 80.0 :

                                                                                            print("you are qualified for Exhaustion");
                                                                                            print("enter on the key Level");
                                                                                            exit();


                                                                                    if finalResult < 80.0 :

                                                                                                print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                                print("the percentage of success probability is not qualified !!");
                                                                                                exit();


                                                                                    #end of functional programming





                                if context == "2" :

                                        
                                        print("we don't have any type of trend in long term one but with trend");
                                        exit();





















                            # intra-day type

                            if term  == "2" :

                                ExhaustionScore += 1;


                                context = input("choose type of context.\n1.(with) trend\n2.counter trend(ranges & corrective zones)\n");

                                if context == "1" :

                                            # (with) trend

                                            ExhaustionScore += 1;


                                            keyCon1 = input("occur after several bars have?\n1.yes\n2.no\n");

                                
                                            if keyCon1 == "1" :


                                                ExhaustionScore += 1;


                                            if keyCon1 == "2" :

                                                ExhaustionScore -= 1;



                                            keyCon2 = input("the largest bar in the series\n1.yes\n2.no\n");


                                            if keyCon2 == "1" :


                                                ExhaustionScore += 1;


                                            if keyCon2 == "2" :

                                                ExhaustionScore -= 1;


                                            keyCon3 = input("occur near key support/resistance level or on the break of one\n1.yes\n2.no\n");
                                                


                                            if keyCon3 == "1" :


                                                ExhaustionScore += 1;


                                            if keyCon3 == "2" :

                                                ExhaustionScore -= 1;


                        ######################################### entry
                                    
                                            if ExhaustionScore >= 5 :
                                
                                            
                                                                        print("conditions are qualified for Exhaustion");
                                                                        #functional programming
                                                                        print("the Exhaustion score is :" + str(ExhaustionScore));

                                                                        # SPP : success probability percentage
                                                                        def SPP (values) :


                                                                            mainValue = (values/totalLTExhaustionScore)*100;

                                                                            return mainValue;

                                                                        finalResult = SPP(ExhaustionScore);


                                                                        if finalResult > 80.0 :

                                                                                print("you are qualified for Exhaustion");
                                                                                print("enter on the key Level");
                                                                                exit();


                                                                        if finalResult < 80.0 :

                                                                                    print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                    print("the percentage of success probability is not qualified !!");
                                                                                    exit();


                                                                        #end of functional programming










                                # CT ( Corrective ranges )

                                if context == "2" :

                                            totalCoHExhaustionScore = 3;
                                            totalCoCTExhaustionScore = 4;


                                            #more common on this type
                                            # corrective zones
                                            # fade them for CT impulsive move and near a key S/R level
                                            # if it's RRL or LLT it adds to it +


                                            ExhaustionScore += 1;
                                            
                                            correctiveZoneType = input("select the corrective zone type : \n1.Horizontal\n2.Counter trend\n");
                                    
                                            
                                            
                                            # Corrective Horizintal 

                                            if correctiveZoneType == "1" :


                                                                            ExhaustionScore += 1;

                                                                            # entry

                                                                            side = input("choose the side.\n1.corrective zones towards the bottom of a down trend\n2.corrective zones towards the top of an up trend");

                                                                            if side == "1" & ExhaustionScore >= 3 :




                                                                                                                    print("sell at the top at the key level");

                                                                                                                    print("conditions are qualified for Exhaustion");
                                                                                                                    #functional programming
                                                                                                                    print("the Exhaustion score is :" + str(ExhaustionScore));

                                                                                                                    # SPP : success probability percentage
                                                                                                                    def SPP (values) :


                                                                                                                        mainValue = (values/totalCoHExhaustionScore)*100;

                                                                                                                        return mainValue;

                                                                                                                    finalResult = SPP(ExhaustionScore);


                                                                                                                    if finalResult > 80.0 :

                                                                                                                            print("you are qualified for Exhaustion");
                                                                                                                            print("enter on the key Level");
                                                                                                                            exit();


                                                                                                                    if finalResult < 80.0 :

                                                                                                                                print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                                                                print("the percentage of success probability is not qualified !!");
                                                                                                                                exit();


                                                                                                                    #end of functional programming






                                                                            if side == "2" & ExhaustionScore >= 3 :





                                                                                                                    print("Buy at the bottom at the key level");

                                                                                                                    print("conditions are qualified for Exhaustion");
                                                                                                                    #functional programming
                                                                                                                    print("the Exhaustion score is :" + str(ExhaustionScore));

                                                                                                                    # SPP : success probability percentage
                                                                                                                    def SPP (values) :


                                                                                                                        mainValue = (values/totalCoHExhaustionScore)*100;

                                                                                                                        return mainValue;

                                                                                                                    finalResult = SPP(ExhaustionScore);


                                                                                                                    if finalResult > 80.0 :

                                                                                                                                print("you are qualified for Exhaustion");
                                                                                                                                print("enter on the key Level");
                                                                                                                                exit();


                                                                                                                    if finalResult < 80.0 :

                                                                                                                                print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                                                                print("the percentage of success probability is not qualified !!");
                                                                                                                                exit();


                                                                                                                    #end of functional programming

















                                            #  Corrective  CT

                                            if correctiveZoneType == "2" :


                                                                            ExhaustionScore += 1;


                                                                            Length = input("is it accured in Medium to Larg corrective structure?\n1.yes\n2.no\n ");

                                                                            if Length == "1" :



                                                                                            ExhaustionScore += 1;


                                                                                            # entry

                                                                                            side = input("choose the side.\n1.corrective zones towards the bottom of a down trend\n2.corrective zones towards the top of an up trend");

                                                                                            if side == "1" & ExhaustionScore >= 4 :




                                                                                                                                    print("sell at the top at the key level");

                                                                                                                                    print("conditions are qualified for Exhaustion");
                                                                                                                                    #functional programming
                                                                                                                                    print("the Exhaustion score is :" + str(ExhaustionScore));

                                                                                                                                    # SPP : success probability percentage
                                                                                                                                    def SPP (values) :


                                                                                                                                        mainValue = (values/totalCoCTExhaustionScore)*100;

                                                                                                                                        return mainValue;

                                                                                                                                    finalResult = SPP(ExhaustionScore);


                                                                                                                                    if finalResult > 80.0 :

                                                                                                                                            print("you are qualified for Exhaustion");
                                                                                                                                            print("enter on the key Level");
                                                                                                                                            exit();


                                                                                                                                    if finalResult < 80.0 :

                                                                                                                                                print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                                                                                print("the percentage of success probability is not qualified !!");
                                                                                                                                                exit();


                                                                                                                                    #end of functional programming






                                                                                            if side == "2" & ExhaustionScore >= 4 :





                                                                                                                                    print("Buy at the bottom at the key level");

                                                                                                                                    print("conditions are qualified for Exhaustion");
                                                                                                                                    #functional programming
                                                                                                                                    print("the Exhaustion score is :" + str(ExhaustionScore));

                                                                                                                                    # SPP : success probability percentage
                                                                                                                                    def SPP (values) :


                                                                                                                                        mainValue = (values/totalCoCTExhaustionScore)*100;

                                                                                                                                        return mainValue;

                                                                                                                                    finalResult = SPP(ExhaustionScore);


                                                                                                                                    if finalResult > 80.0 :

                                                                                                                                            print("you are qualified for Exhaustion");
                                                                                                                                            print("enter on the key Level");
                                                                                                                                            exit();


                                                                                                                                    if finalResult < 80.0 :

                                                                                                                                                print("the percentage of success probabilty is : " + str(finalResult) );
                                                                                                                                                print("the percentage of success probability is not qualified !!");
                                                                                                                                                exit();


                                                                                                                                    #end of functional programming








                                                                            if Length == "2" :



                                                                                            ExhaustionScore -= 1;
                                                                                            print("not qualified for this type of Exhaustion");
                                                                                            
                        return ExhaustionScore;                






                   
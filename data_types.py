def data_type(x):
  if x == int:
   if x < 100:
   	return "less than 100"
   elif x > 100:
   	return "more than 100"
   else:
   	return "equal to 100"
  elif (x) == str:
    return len(x)
  elif (x) == None:
    return "no value"
  elif x == True:
    return "True"
  elif x == False:
    return "False"
  elif x == lst:
 	  return {2}
  else:
    return None
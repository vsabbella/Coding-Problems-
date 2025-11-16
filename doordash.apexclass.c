

Director  A:
  - Manager - A: 
    - Rep A
Director B:
  - Manager - B:
    - Rep B

    Director A, Manager - , Rep A

 Map<Id,List<Id>> userroleIdMap = new Map<Id,List<Id>>()
 for(Userrole ur: [Select id,name,parentId from userrole  ]){
     
     if(userroleIdMap.containsKey(ur.parentId))
        userroleIdMap.get(ur.parentId).add(Id);
     else
         userroleIdMap.put(new List<Id>{Id});
     

 }    

 // Director A -> (Manager -A)
 //Manager - A -> (Rep -A) (Rep -B)

 List<Id> roleIds = new List<Id>();
 roleIds.addALl(userroleIdMap.get(directorId));
 
 /*
    Director A - [Manager - A]

    for(role r: Director A. Children):
        r.getChilderen
 
 
 
 
 */
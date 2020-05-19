bank_side1 = []
bank_side2 = []
boat = []


# In[26]:


bank_side1.append("goat")
bank_side1.append("grass")
bank_side1.append("tiger")
boat.append("man")
print("intially on bank 1 of river:\n", bank_side1)


# In[27]:


boat.append("goat")
print("on boat:\n", boat)
print("After first trip of boat from bank 1 to bank 2:")
bank_side2.append(bank_side1.pop(0))
print("On bank 1:\n",bank_side1)
print("On bank 2:\n",bank_side2)
print("****------****")


# In[28]:


boat.pop(1)
boat.append("grass")
print("on boat:\n", boat)
print("After second trip of boat from bank 1 to bank 2:")
bank_side2.append(bank_side1.pop(0))
print("On bank 1:\n",bank_side1)
print("On bank 2:\n",bank_side2)
print("****------****")


# In[29]:


boat.pop(1)
boat.append("goat")
print("on boat:\n", boat)
print("After second trip of boat from bank 2 to bank 1:")
bank_side2.pop(0)
bank_side1.append("goat")
print("On bank 1:\n",bank_side1)
print("On bank 2:\n",bank_side2)
print("****------****")


# In[30]:


boat.pop(1)
boat.append("tiger")
print("on boat:\n", boat)
print("After third trip of boat from bank 1 to bank 2:")
bank_side2.append(bank_side1.pop(0))
print("On bank 1:\n",bank_side1)
print("On bank 2:\n",bank_side2)
print("****------****")


# In[31]:


boat.pop(1)
boat.append("goat")
print("on boat:\n", boat)
print("After fourth trip of boat from bank 1 to bank 2:")
bank_side2.append(bank_side1.pop(0))
print("On bank 1:\n",bank_side1)
print("On bank 2:\n",bank_side2)
print("****------****")


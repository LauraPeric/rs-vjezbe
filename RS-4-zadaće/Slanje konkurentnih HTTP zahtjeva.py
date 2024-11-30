'''1. Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.'''


import aiohttp
import asyncio
import time

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    async with session.get(url) as response:
        return await response.json()

async def main():
    start_time = time.time() 
    
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(
            fetch_users(session),
            fetch_users(session),
            fetch_users(session),
            fetch_users(session),
            fetch_users(session)
        )
    names = [user['name'] for user in responses[0]]
    emails = [user['email'] for user in responses[0]]
    usernames = [user['username'] for user in responses[0]]
    
    end_time = time.time()

    print("names:", names)
    print("emails:", emails)
    print("usernames:", usernames)
    print(f"execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


'''
2. Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact . Izradite 20
Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
pohranite odjednom koristeći asyncio.gather funkciju. 

Druga korutina filter_cat_facts ne šalje HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).
Primjer konačnog ispisa:
Filtrirane činjenice o mačkama:
- A 2007 Gallup poll revealed that both men and women were equally likely to own a cat.
- The first cat in space was a French cat named Felicette (a.k.a. “Astrocat”) In 1963,
France blasted the cat into outer space. Electrodes implanted in her brains sent
neurological signals back to Earth. She survived the trip.
- The lightest cat on record is a blue point Himalayan called Tinker Toy, who weighed 1
pound, 6 ounces (616 g). Tinker Toy was 2.75 inches (7 cm) tall and 7.5 inches (19 cm)
long.
- The first commercially cloned pet was a cat named "Little Nicky." He cost his owner
$50,000, making him one of the most expensive cats ever.
- In the 1750s, Europeans introduced cats into the Americas to control pests.
- A group of cats is called a clowder.'''


import re

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict['fact']  # Vraćamo činjenicu


async def filter_cat_facts(facts):
    return [fact for fact in facts if re.search(r'\bcat\b', fact, re.IGNORECASE)]


async def main():
    start_time = time.time() 
    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session) for _ in range(20)] 
        facts = await asyncio.gather(*tasks)
        filtered_facts = await filter_cat_facts(facts)
    
        print("filtrirane činjenice o mačkama:")
        for fact in filtered_facts:
            print(f"- {fact}")
            
    end_time = time.time()
    print(f"vrijeme izvođenja: {end_time - start_time:.2f} sekundi")

if __name__ == "__main__":
    asyncio.run(main())


'''3. Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
URL: https://catfact.ninja/fact .
Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
*cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
zip(dog_facts, cat_facts) .
Primjer konačnog ispisa:
Mixane činjenice o psima i mačkama:
If they have ample water, cats can tolerate temperatures up to 133 °F.
Dogs with little human contact in the first three months typically don’t make good pets.
The most popular dog breed in Canada, U.S., and Great Britain is the Labrador retriever.
An estimated 1,000,000 dogs in the U.S. have been named as the primary beneficiaries in
their owner’s will.
When a cats rubs up against you, the cat is marking you with it's scent claiming
ownership.'''

import aiohttp
import asyncio
import time

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    fact_dict = await response.json()
    return fact_dict['fact']

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json
    return fact_dict['fact']

async def mix_facts(dog_facts, cat_facts):
    mixed_facts= []
    for dog_fact, cat_fact in zip(dog_facts,cat_facts):
        if len(dog_fact) > len(cat_fact):
            mixed_facts.append(dog_fact)
        else:
            mixed_facts.append(cat_fact)
    return mix_facts

async def main():
 start_time = time.time()
 async with aiohttp.ClientSession() as session:
    cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]
    dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]

    dog_facts, cat_facts = await asyncio.gather(*cat_facts_tasks,dog_facts_tasks)

    mix_facts = await mix_facts(dog_facts, cat_facts)
   
 end_time = time.time()
 print("pomjesane cinjenice o psima i mackama:")
 for fact in mix_facts:
    print(f"- {fact}")
 print(f"vrijeme izvođenja: {end_time - start_time:.2f} sekundi")


if __name__ == '__main__':
    asyncio.run(main())
o
    ??c?  ?                   @   s4   d d? Z dd? Zdd? Zdd? Zeedd	d
?? dS )c                 C   s   d| | | ? ?S )NzObwod trojkata to : ? ??a?b?cr   r   ?Kc:\Users\bruno\OneDrive\Pulpit\FirstSemester\python_listy\szosta\trojkat.py?	obwodTroj   s   r   c                 C   s6   | | | d }d|||   ||  ||  d ? ?S )N?   zPole trojkata to : g      ??r   )r   r   r   ?pr   r   r   ?poleTroj   s   &r
   c                 C   s\   | |  kr|krdS  | |ks||ks| |krdS | |kr(| |kr*||kr,dS d S d S d S )NzTrojkat jest rownobocznyzTrojkat jest rownoramiennyzTrojkat jest roznobocznyr   r   r   r   r   ?rodzajTrojBok   s   ??r   c                 C   sV   | ||g}|? ?  | d |d  }||d k rdS ||d kr!dS ||d kr)dS d S )Nr   zTrojkat jest rozwartokatnyzTrojkat jest ostrokatnyzTrojkat jest prostokatny)?sort)r   r   r   ZbokiZkwMniejr   r   r   ?rodzajTrojKat   s   
?r   ?   ?   r   N)r   r
   r   r   ?printr   r   r   r   ?<module>   s
    
document.addEventListener('DOMContentLoaded', () => {
  let currentYear = new Date().getFullYear();
  const currentYearSpan = document.getElementById('current-year');
  const calendarContainer = document.getElementById('year-calendar');
  const zoneSelector = document.getElementById('zone-selector');
  let selectedCell = null;

  // Affiche l'année actuelle
  currentYearSpan.textContent = currentYear;

  // Navigation entre années
  document.getElementById('prev-year').addEventListener('click', () => {
    currentYear--;
    updateYear();
  });

  document.getElementById('next-year').addEventListener('click', () => {
    currentYear++;
    updateYear();
  });

  // Gestion du changement de zone scolaire
  zoneSelector.addEventListener('change', () => {
    updateYear();
  });

  // Met à jour l'affichage de l'année et recharge les événements
  function updateYear() {
    currentYearSpan.textContent = currentYear;
    fetchEvents(currentYear, zoneSelector.value);
  }

  // Récupère les événements depuis Django
  async function fetchEvents(year, zone = 'A') {
    try {
      const response = await fetch(`/calendar/get-events/?year=${year}&zone=${zone}`);
      if (!response.ok) throw new Error('Erreur réseau');
      const events = await response.json();
      renderCalendar(events, year);
    } catch (error) {
      console.error('Erreur lors de la récupération des événements :', error);
      // Sécurisé contre XSS - Création d'élément au lieu d'innerHTML
      const errorParagraph = document.createElement('p');
      errorParagraph.className = 'text-danger text-center';
      errorParagraph.textContent = 'Erreur de chargement des événements.';
      calendarContainer.appendChild(errorParagraph);
    }
  }

  // Crée un gestionnaire de clic pour un jour
  function createClickHandler(year, month, day, cell) {
    return () => {
      if (selectedCell) selectedCell.classList.remove('table-primary');
      cell.classList.add('table-primary');
      selectedCell = cell;
      window.location.href = `/calendar/daily-schedule/${year}/${month}/${day}/`;
    };
  }

  // Génère l'ensemble des 12 mois avec leurs jours
  function renderCalendar(events, year) {
    // Sécurisé - Vider le contenu sans innerHTML
    while (calendarContainer.firstChild) {
      calendarContainer.removeChild(calendarContainer.firstChild);
    }

    for (let month = 0; month < 12; month++) {
      // Crée la carte du mois
      const monthCard = document.createElement('div');
      monthCard.className = 'month-card';

      // Nom du mois avec majuscule
      const monthName = new Date(year, month).toLocaleString('fr-FR', { month: 'long' });
      const monthTitle = monthName.charAt(0).toUpperCase() + monthName.slice(1);

      // Structure HTML améliorée avec les nouvelles classes - Sécurisé contre XSS
      const monthHeader = document.createElement('div');
      monthHeader.className = 'month-header';
      monthHeader.textContent = monthTitle;
      
      const cardBody = document.createElement('div');
      cardBody.className = 'card-body';
      
      const table = document.createElement('table');
      table.className = 'calendar-table';
      table.setAttribute('aria-label', `Calendrier ${monthTitle} ${year}`);
      
      const thead = document.createElement('thead');
      const headerRow = document.createElement('tr');
      const dayNames = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'];
      dayNames.forEach(dayName => {
        const th = document.createElement('th');
        th.textContent = dayName;
        headerRow.appendChild(th);
      });
      thead.appendChild(headerRow);
      
      const tbody = document.createElement('tbody');
      
      table.appendChild(thead);
      table.appendChild(tbody);
      cardBody.appendChild(table);
      
      monthCard.appendChild(monthHeader);
      monthCard.appendChild(cardBody);

      // Référence au tbody pour ajouter les jours (déjà créé ci-dessus)

      // Calcul du premier jour (Lundi=0)
      let firstDay = new Date(year, month, 1).getDay();
      firstDay = (firstDay === 0) ? 6 : firstDay - 1;

      // Nombre de jours dans le mois
      const daysInMonth = new Date(year, month + 1, 0).getDate();
      let day = 1;
      
      // Date d'aujourd'hui pour marquer le jour actuel
      const today = new Date();
      const isCurrentYear = today.getFullYear() === year;
      const isCurrentMonth = today.getMonth() === month;
      const todayDay = today.getDate();

      // Création des lignes et cellules
      for (let week = 0; week < 6; week++) {
        const row = document.createElement('tr');

        for (let i = 0; i < 7; i++) {
          const cell = document.createElement('td');

          if (week === 0 && i < firstDay) {
            // Jours du mois précédent
            cell.classList.add('other-month');
            const prevMonthDay = new Date(year, month, 0).getDate() - (firstDay - i - 1);
            const dayDiv = document.createElement('div');
            dayDiv.className = 'day-number';
            dayDiv.textContent = prevMonthDay;
            cell.appendChild(dayDiv);
          } else if (day > daysInMonth) {
            // Jours du mois suivant
            cell.classList.add('other-month');
            const nextMonthDay = day - daysInMonth;
            const dayDiv = document.createElement('div');
            dayDiv.className = 'day-number';
            dayDiv.textContent = nextMonthDay;
            cell.appendChild(dayDiv);
            day++;
          } else {
            const currentDate = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
            
            // Créer le numéro du jour
            const dayNumber = document.createElement('div');
            dayNumber.className = 'day-number';
            dayNumber.textContent = day;
            
            // Marquer le jour actuel
            if (isCurrentYear && isCurrentMonth && day === todayDay) {
              cell.classList.add('today');
            }
            
            cell.appendChild(dayNumber);

            // Trouve les événements correspondant à ce jour
            const dayEvents = events.filter(event => event.date === currentDate);

            // Séparer les fiches et les vacances
            const ficheEvents = dayEvents.filter(event => event.type === 'fiche');
            const holidayEvents = dayEvents.filter(event => event.type === 'holiday');

            // Ajouter une classe spéciale si c'est un jour de vacances
            if (holidayEvents.length > 0) {
              cell.classList.add('holiday-day');
            }

            // Afficher les fiches comme des points bleus discrets
            if (ficheEvents.length > 0) {
              const ficheIndicator = document.createElement('div');
              ficheIndicator.className = 'fiche-indicator';
              
              // Tooltip avec les informations des séances
              if (ficheEvents.length === 1) {
                const event = ficheEvents[0];
                if (event.description) {
                  ficheIndicator.setAttribute('data-tooltip', `${event.title} - ${event.description}`);
                } else {
                  ficheIndicator.setAttribute('data-tooltip', event.title);
                }
              } else {
                ficheIndicator.setAttribute('data-tooltip', `${ficheEvents.length} séances ce jour`);
              }
              
              cell.appendChild(ficheIndicator);
            }

            // Ajouter un indicateur discret pour les vacances
            if (holidayEvents.length > 0) {
              const holidayIndicator = document.createElement('div');
              holidayIndicator.className = 'holiday-indicator';
              holidayIndicator.setAttribute('data-tooltip', `${holidayEvents[0].title} - ${holidayEvents[0].description}`);
              cell.appendChild(holidayIndicator);
            }

            // Ajoute le clic pour aller vers la fiche journalière
            cell.style.cursor = 'pointer';
            cell.addEventListener('click', createClickHandler(year, month + 1, day, cell));

            day++;
          }

          row.appendChild(cell);
        }

        tbody.appendChild(row);

        if (day > daysInMonth) break; // Stop après le dernier jour
      }

      calendarContainer.appendChild(monthCard);
    }
  }

  // Initialisation
  fetchEvents(currentYear, zoneSelector.value);
});

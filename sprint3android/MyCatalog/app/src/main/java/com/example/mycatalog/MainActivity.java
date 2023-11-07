package com.example.mycatalog;

import android.os.Bundle;
import android.view.MenuItem;


import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import com.google.android.material.navigation.NavigationView;

// La clase MainActivity se extiende de AppCompatActivity y usa la interfaz NavigationView.OnNavigationItemSelectedListener
// para manejar los eventos de selección de elementos en la navegación.
public class MainActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {

    // onCreate es el primer método que se llama en el ciclo de vida de la actividad.
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Establece la vista de la actividad desde el archivo de layout XML.
        setContentView(R.layout.main_activity);

        // Encuentra la barra de herramientas definida en el layout y la establece como la barra de acciones para esta actividad.
        Toolbar toolbar = findViewById(R.id.toolbar);

        // Encuentra el DrawerLayout que permitirá mostrar el menú de navegación deslizable.
        DrawerLayout drawer = findViewById(R.id.drawer_layout);

        // Crea un botón de alternancia para que el menú de navegación se pueda abrir y cerrar.
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);

        // Agrega un listener al DrawerLayout para responder a los eventos de apertura y cierre del menú.
        drawer.addDrawerListener(toggle);

        // Sincroniza el estado del botón de alternancia después de que se haya agregado el listener.
        toggle.syncState();

        // Encuentra la NavigationView y establece esta clase como la que manejará los eventos de selección de elementos.
        NavigationView navigationView = findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
    }

    // Este método se llama cada vez que se selecciona un elemento en el menú de navegación.
    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        // Inicializa el fragmento que se mostrará como null al principio.
        Fragment fragment = null;

        // Obtiene el ID del elemento seleccionado en el menú.
        int id = item.getItemId();

        // Comprueba el ID del elemento seleccionado y crea el fragmento correspondiente.
        if (id == R.id.nav_fragment1) {
            fragment = new AboutFragment(); // Crea un fragmento AboutFragment si se selecciona la primera opción.
        } else if (id == R.id.nav_fragment2) {
            fragment = new CatalogActivity(); // Crea un CatalogActivity si se selecciona la segunda opción.
        }

        // Si ningún fragmento fue seleccionado, selecciona AboutFragment como predeterminado.
        if (fragment == null){
            fragment = new AboutFragment();
        }

        // Si se seleccionó un fragmento, reemplaza el contenido actual con el nuevo fragmento.
        if (fragment != null) {
            getSupportFragmentManager().beginTransaction()
                    .replace(R.id.nav_host_fragment, fragment)
                    .commit();
        }

        // Cierra el menú de navegación una vez que se selecciona un elemento.
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);

        // Devuelve true porque el evento de selección ha sido manejado.
        return true;
    }

}
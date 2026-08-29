# Prompt para AI Studio #24: Barra de Filtro de Personaje Superior + Tema de Color Dinámico + Filtrado en Ficha de Inicio (SummaryScreen)

## 📋 Contexto y Objetivo
Se requiere actualizar la aplicación Kotlin Compose **LV-App** para:
1. Agregar una **Barra de Filtro de Personaje Superior (`CharacterTopFilterBar`)** permanente debajo de la `TopAppBar` en `LaVouteApp.kt` con las opciones: `Todas` (🏛️), `Ele` (🎀), `Miss Doll` (💅) y `Anaïs` (👑).
2. **Persistir** la selección de personaje en `SharedPreferences` vía `MainViewModel.kt`.
3. **Cambiar dinámicamente el tema de color (`MaterialTheme`)** de toda la app según el personaje seleccionado:
   - **Todas**: Gold Noir & Mint Teal (`SolidGold` `#FFC107` / `MintTeal` `#00BFA5`).
   - **Ele**: Hot Magenta & Fuchsia (`ElePrimary` `#FF007F` / `EleSecondary` `#FF4081`).
   - **Miss Doll**: High-Gloss Cerise Pink & Ice Cyan (`MissDollPrimary` `#FF1493` / `MissDollSecondary` `#00E5FF`).
   - **Anaïs**: Imperial Crimson & Velvet Gold (`AnaisPrimary` `#C62828` / `AnaisSecondary` `#D4AF37`).
4. **Filtrar la Ficha de Inicio (`SummaryScreen.kt`)** de forma dinámica según el personaje seleccionado (totales, tarjetas, barra de progreso y distintivo por personaje).

---

## 🛠️ Instrucciones de Modificación por Archivo

### 1. `app/src/main/java/com/example/ui/theme/Color.kt`
Agregar las definiciones de color para los 3 personajes:

```kotlin
// Character Theme Palettes
// 1. Ele (Hot Magenta & Fuchsia)
val ElePrimary = Color(0xFFFF007F)
val EleSecondary = Color(0xFFFF4081)
val EleTertiary = Color(0xFFD81B60)
val EleBackground = Color(0xFF0D030B)
val EleSurface = Color(0xFF1B0916)
val EleSurfaceLight = Color(0xFF2A1024)

// 2. Miss Doll (High-Gloss Cerise Pink & Ice Cyan)
val MissDollPrimary = Color(0xFFFF1493)
val MissDollSecondary = Color(0xFF00E5FF)
val MissDollTertiary = Color(0xFFFF2A85)
val MissDollBackground = Color(0xFF03090F)
val MissDollSurface = Color(0xFF0C161F)
val MissDollSurfaceLight = Color(0xFF162432)

// 3. Anaïs (Imperial Crimson & Velvet Gold)
val AnaisPrimary = Color(0xFFC62828)
val AnaisSecondary = Color(0xFFD4AF37)
val AnaisTertiary = Color(0xFF8B0000)
val AnaisBackground = Color(0xFF0A0204)
val AnaisSurface = Color(0xFF1B0609)
val AnaisSurfaceLight = Color(0xFF2D0B0F)
```

---

### 2. `app/src/main/java/com/example/ui/theme/Theme.kt`
Actualizar `Theme.kt` para crear paletas `darkColorScheme` por personaje y hacer que `MyApplicationTheme` reciba el parámetro `characterFilter`:

```kotlin
package com.example.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val DarkColorScheme = darkColorScheme(
    primary = SolidGold,
    secondary = MintTeal,
    tertiary = HotMagentaAccent,
    background = DeepVelvetBg,
    surface = VelvetCard,
    onPrimary = Color.Black,
    onSecondary = Color.White,
    onTertiary = Color.White,
    onBackground = Color.White,
    onSurface = Color.White,
    surfaceVariant = VelvetCardLight,
    onSurfaceVariant = TextGray,
    outline = VelvetBorder
)

private val EleColorScheme = darkColorScheme(
    primary = ElePrimary,
    secondary = EleSecondary,
    tertiary = EleTertiary,
    background = EleBackground,
    surface = EleSurface,
    onPrimary = Color.White,
    onSecondary = Color.White,
    onTertiary = Color.White,
    onBackground = Color.White,
    onSurface = Color.White,
    surfaceVariant = EleSurfaceLight,
    onSurfaceVariant = TextGray,
    outline = ElePrimary.copy(alpha = 0.5f)
)

private val MissDollColorScheme = darkColorScheme(
    primary = MissDollPrimary,
    secondary = MissDollSecondary,
    tertiary = MissDollTertiary,
    background = MissDollBackground,
    surface = MissDollSurface,
    onPrimary = Color.White,
    onSecondary = Color.Black,
    onTertiary = Color.White,
    onBackground = Color.White,
    onSurface = Color.White,
    surfaceVariant = MissDollSurfaceLight,
    onSurfaceVariant = TextGray,
    outline = MissDollSecondary.copy(alpha = 0.5f)
)

private val AnaisColorScheme = darkColorScheme(
    primary = AnaisPrimary,
    secondary = AnaisSecondary,
    tertiary = AnaisTertiary,
    background = AnaisBackground,
    surface = AnaisSurface,
    onPrimary = Color.White,
    onSecondary = Color.Black,
    onTertiary = Color.White,
    onBackground = Color.White,
    onSurface = Color.White,
    surfaceVariant = AnaisSurfaceLight,
    onSurfaceVariant = TextGray,
    outline = AnaisSecondary.copy(alpha = 0.5f)
)

fun getColorSchemeForCharacter(characterFilter: String) = when (characterFilter) {
    "Ele" -> EleColorScheme
    "Miss Doll" -> MissDollColorScheme
    "Anaïs" -> AnaisColorScheme
    else -> DarkColorScheme
}

@Composable
fun MyApplicationTheme(
    characterFilter: String = "Todas",
    darkTheme: Boolean = true,
    dynamicColor: Boolean = false,
    content: @Composable () -> Unit,
) {
    val colorScheme = getColorSchemeForCharacter(characterFilter)
    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        content = content
    )
}
```

---

### 3. `app/src/main/java/com/example/ui/viewmodel/MainViewModel.kt`
Asegurar la persistencia del filtro de personaje en `SharedPreferences`:

```kotlin
    private val _selectedCharacterFilter = MutableStateFlow(
        prefs.getString("selected_character_filter", "Todas") ?: "Todas"
    )
    val selectedCharacterFilter: StateFlow<String> = _selectedCharacterFilter.asStateFlow()
    fun setCharacterFilter(filter: String) {
        _selectedCharacterFilter.value = filter
        prefs.edit().putString("selected_character_filter", filter).apply()
    }
```

---

### 4. `app/src/main/java/com/example/ui/LaVouteApp.kt`
Observar `selectedCharacterFilter`, envolver el layout en `MyApplicationTheme(characterFilter = selectedCharacterFilter)` y colocar la barra `CharacterTopFilterBar` en `topBar`:

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LaVouteApp(
    viewModel: MainViewModel,
    modifier: Modifier = Modifier
) {
    val selectedTab by viewModel.selectedTab.collectAsState()
    val syncState by viewModel.syncState.collectAsState()
    val allLooks by viewModel.allLooks.collectAsState()
    val selectedCharacterFilter by viewModel.selectedCharacterFilter.collectAsState()

    MyApplicationTheme(characterFilter = selectedCharacterFilter) {
        val sharedUri = viewModel.sharedImageUri.value
        if (sharedUri != null) {
            ShareAssignmentScreen(viewModel = viewModel, uri = sharedUri as android.net.Uri) {
                viewModel.sharedImageUri.value = null
            }
        } else {
            Scaffold(
                modifier = modifier.fillMaxSize(),
                topBar = {
                    Column {
                        TopAppBar(
                            title = {
                                Row(
                                    verticalAlignment = Alignment.CenterVertically,
                                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                                ) {
                                    Text(
                                        text = when (selectedCharacterFilter) {
                                            "Ele" -> "🎀"
                                            "Miss Doll" -> "💅"
                                            "Anaïs" -> "👑"
                                            else -> "🍷"
                                        },
                                        fontSize = 24.sp
                                    )
                                    Column {
                                        Text(
                                            "LA VOÛTE",
                                            style = MaterialTheme.typography.titleMedium.copy(
                                                fontWeight = FontWeight.ExtraBold,
                                                letterSpacing = 2.sp,
                                                color = Color.White
                                            )
                                        )
                                        Text(
                                            "Vault de d'Anaïs v${com.example.BuildConfig.VERSION_NAME} (${com.example.BuildConfig.VERSION_CODE}) · ${com.example.BuildConfig.GIT_SHA}",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                color = MaterialTheme.colorScheme.primary,
                                                fontWeight = FontWeight.Bold
                                            )
                                        )
                                    }
                                }
                            },
                            actions = {
                                IconButton(
                                    onClick = { viewModel.triggerSync() },
                                    enabled = syncState !is SyncState.Syncing,
                                    modifier = Modifier.testTag("sync_button")
                                ) {
                                    if (syncState is SyncState.Syncing) {
                                        CircularProgressIndicator(
                                            modifier = Modifier.size(24.dp),
                                            strokeWidth = 2.dp,
                                            color = MaterialTheme.colorScheme.primary
                                        )
                                    } else {
                                        Icon(
                                            imageVector = Icons.Default.Refresh,
                                            contentDescription = "Sincronizar",
                                            tint = MaterialTheme.colorScheme.primary
                                        )
                                    }
                                }
                            },
                            colors = TopAppBarDefaults.topAppBarColors(
                                containerColor = MaterialTheme.colorScheme.background,
                                titleContentColor = Color.White
                            )
                        )

                        // Top Character Filter Bar
                        CharacterTopFilterBar(
                            selectedCharacter = selectedCharacterFilter,
                            onCharacterSelected = { viewModel.setCharacterFilter(it) }
                        )
                    }
                },
                ...
```

Y agregar el composable `CharacterTopFilterBar`:

```kotlin
@Composable
fun CharacterTopFilterBar(
    selectedCharacter: String,
    onCharacterSelected: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    val characters = listOf(
        CharacterChipData("Todas", "🏛️", SolidGold),
        CharacterChipData("Ele", "🎀", ElePrimary),
        CharacterChipData("Miss Doll", "💅", MissDollPrimary),
        CharacterChipData("Anaïs", "👑", AnaisPrimary)
    )

    Surface(
        color = VelvetCardLight.copy(alpha = 0.85f),
        tonalElevation = 4.dp,
        modifier = modifier
            .fillMaxWidth()
            .border(
                width = (0.5).dp,
                color = MaterialTheme.colorScheme.primary.copy(alpha = 0.25f)
            )
    ) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 8.dp, vertical = 4.dp),
            horizontalArrangement = Arrangement.SpaceEvenly,
            verticalAlignment = Alignment.CenterVertically
        ) {
            characters.forEach { chip ->
                val isSelected = selectedCharacter == chip.name
                val accentColor = chip.color

                FilterChip(
                    selected = isSelected,
                    onClick = { onCharacterSelected(chip.name) },
                    label = {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(4.dp)
                        ) {
                            Text(chip.emoji, fontSize = 13.sp)
                            Text(
                                chip.name,
                                fontWeight = if (isSelected) FontWeight.ExtraBold else FontWeight.SemiBold,
                                fontSize = 11.sp
                            )
                        }
                    },
                    colors = FilterChipDefaults.filterChipColors(
                        selectedContainerColor = accentColor.copy(alpha = 0.3f),
                        selectedLabelColor = Color.White,
                        containerColor = Color.Transparent,
                        labelColor = Color.Gray
                    ),
                    border = FilterChipDefaults.filterChipBorder(
                        enabled = true,
                        selected = isSelected,
                        borderColor = Color.White.copy(alpha = 0.1f),
                        selectedBorderColor = accentColor,
                        borderWidth = 1.dp,
                        selectedBorderWidth = 1.5.dp
                    ),
                    shape = RoundedCornerShape(16.dp)
                )
            }
        }
    }
}

private data class CharacterChipData(
    val name: String,
    val emoji: String,
    val color: Color
)
```

---

### 5. `app/src/main/java/com/example/ui/SummaryScreen.kt`
En `SummaryScreen.kt`, filtrar los looks por `selectedCharacterFilter` y usar `MaterialTheme.colorScheme.primary`:

```kotlin
@Composable
fun SummaryScreen(
    viewModel: MainViewModel,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val prefs = remember { context.getSharedPreferences("app_prefs", Context.MODE_PRIVATE) }

    val selectedCharacterFilter by viewModel.selectedCharacterFilter.collectAsState()
    val allLooks: List<LookEntity> by viewModel.allLooks.collectAsState(initial = emptyList())
    val allPrompts: List<com.example.data.local.PromptEntity> by viewModel.allPrompts.collectAsState(initial = emptyList())
    val allImages: List<ImageEntity> by viewModel.allImages.collectAsState(initial = emptyList())

    // Character Filtered Looks
    val characterFilteredLooks = remember(allLooks, selectedCharacterFilter) {
        if (selectedCharacterFilter == "Todas") {
            allLooks
        } else {
            val targetSlug = when (selectedCharacterFilter) {
                "Ele" -> "ele"
                "Miss Doll" -> "miss_doll"
                "Anaïs" -> "anais"
                else -> "ele"
            }
            allLooks.filter { it.characterSlug == targetSlug }
        }
    }

    // Process data
    val lookMissingInfo = remember(characterFilteredLooks, allPrompts, allImages) {
        characterFilteredLooks.map { look ->
            val lookPrompts = allPrompts.filter { it.lookNumber == look.number }
            val lookImages = allImages.filter { it.lookNumber == look.number }
            val missing = mutableListOf<String>()

            val profile = com.example.util.CharacterProfile.ALL.firstOrNull { it.slug == look.characterSlug }
                ?: com.example.util.CharacterProfile.ALL.first { it.slug == "ele" }

            for (p in lookPrompts) {
                val hasImage = lookImages.any { img -> com.example.util.PoseMatcher.matches(p.poseName, img.poseName, profile, look.isBoudoir) }
                if (!hasImage) {
                    missing.add(p.poseName)
                }
            }
            MissingImageInfo(look, missing, lookPrompts.size, lookPrompts.size - missing.size)
        }
    }
```

---

## 🎯 Verificación
- Confirmar que compila con `./gradlew assembleDebug`.
- Verificar el cambio dinamico de color y filtrado instantáneo al seleccionar cada personaje.

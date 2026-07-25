# Updates H1 and adds 4 H2 content sections to all 12 index.html files

DATA = {
    'index.html': {
        'h1': 'Base64 Decoder Online',
        's1_h2': 'What is Base64 Decoding?',
        's1_p': [
            'Base64 decoding is the reverse of Base64 encoding — it converts a Base64 string back into its original binary or text data. Given a valid Base64 string, any decoder can reconstruct the original data without any key or password, which is why Base64 is not a form of encryption.',
            'Base64 encoded data is commonly encountered in JWT tokens (where header and payload are Base64URL encoded), email attachments transmitted via MIME, image Data URIs embedded in HTML and CSS, binary data returned by REST APIs in JSON responses, and configuration files that store binary values as text.',
            'When decoding, it is important to know the original character encoding of the text data. If the original text was UTF-8 (the most common case), selecting UTF-8 or AUTO-DETECT will produce correct results. For legacy systems, you may need to select ISO-8859-1 or Windows-1252 to correctly decode accented characters and special symbols.',
        ],
        's2_h2': 'How to Decode Base64 Online',
        's2_p': [
            'To decode a Base64 string with decodeb64.com, paste your encoded string into the input field and click Decode. The tool automatically strips whitespace and line breaks from the input before decoding, so you do not need to clean the string manually. The decoded output appears in the result field, ready to copy.',
            'If you are decoding a Base64URL string (which uses - and _ instead of + and /), the tool handles this automatically — no manual replacement needed. If the character encoding of the original text is unknown, select AUTO-DETECT and the tool will attempt to identify the correct charset from the decoded bytes.',
            'For batch decoding, enable the "Decode each line separately" option. Each line of your input will be decoded independently, which is useful when you have multiple Base64 entries separated by newlines, such as a list of encoded API tokens or identifiers.',
        ],
        's3_h2': 'Decode Base64URL and JWT Tokens',
        's3_p': [
            'JWT (JSON Web Tokens) consist of three parts separated by dots: header.payload.signature. The header and payload are Base64URL encoded — not standard Base64. Base64URL uses - instead of + and _ instead of /, and omits the = padding character. Standard Base64 decoders will fail on JWT strings unless they handle this variant automatically.',
            'decodeb64.com automatically detects and handles Base64URL input. To inspect a JWT token, paste the full token, then use the "Decode each line separately" option with a dot as the line separator — or simply paste just the header or payload portion (the text before the first or second dot).',
            'Note that decoding a JWT payload reveals the claims it contains (user ID, expiration time, roles, etc.) but does not verify the signature. For security validation, always verify the JWT signature using the appropriate library for your programming language.',
        ],
        's4_h2': 'Decode Base64 Files and Binary Data',
        's4_p': [
            'For encoded files, decodeb64.com includes a file decode section that accepts Base64-encoded .txt files. Upload the file containing the Base64 string, and the tool will decode it back to the original binary content. The file type is automatically detected from the decoded binary using magic byte signatures — PNG header bytes, JPEG SOI marker, GIF signature, WebP RIFF header, and others — so the downloaded file will have the correct extension.',
            'This is useful for recovering files that were encoded for transmission in email or API responses, extracting images embedded as Base64 in configuration files, and decoding binary data stored in databases or log files as Base64 strings.',
            'A security reminder: always verify the source of Base64 data before decoding and executing files. Base64 encoding is sometimes used to obfuscate malicious payloads. Never execute a decoded file from an untrusted source.',
        ],
    },
    'es/index.html': {
        'h1': 'Decodificador Base64 Online',
        's1_h2': '¿Qué es la Decodificación Base64?',
        's1_p': [
            'La decodificación Base64 es la inversa de la codificación Base64 — convierte una cadena Base64 de vuelta a sus datos binarios o de texto originales. Dado una cadena Base64 válida, cualquier decodificador puede reconstruir los datos originales sin ninguna clave ni contraseña, por lo que Base64 no es una forma de cifrado.',
            'Los datos codificados en Base64 se encuentran comúnmente en tokens JWT, archivos adjuntos de correo electrónico transmitidos via MIME, Data URIs de imágenes incrustadas en HTML y CSS, datos binarios devueltos por APIs REST en respuestas JSON, y archivos de configuración que almacenan valores binarios como texto.',
            'Al decodificar, es importante conocer la codificación de caracteres original. Si el texto original era UTF-8, seleccionar UTF-8 o AUTO-DETECT producirá resultados correctos.',
        ],
        's2_h2': 'Cómo Decodificar Base64 Online',
        's2_p': [
            'Para decodificar una cadena Base64 con decodeb64.com, pega tu cadena codificada en el campo de entrada y haz clic en Decodificar. La herramienta elimina automáticamente los espacios y saltos de línea antes de decodificar, por lo que no necesitas limpiar la cadena manualmente.',
            'Si decodificas una cadena Base64URL (que usa - y _ en lugar de + y /), la herramienta lo maneja automáticamente. Si se desconoce la codificación de caracteres del texto original, selecciona AUTO-DETECT.',
            'Para la decodificación por lotes, activa "Decodificar cada línea por separado" — cada línea se decodificará de forma independiente, útil para listas de tokens o identificadores codificados.',
        ],
        's3_h2': 'Decodificar Base64URL y Tokens JWT',
        's3_p': [
            'Los JWT (JSON Web Tokens) constan de tres partes separadas por puntos: encabezado.carga_útil.firma. El encabezado y la carga útil están codificados en Base64URL — no en Base64 estándar. Base64URL usa - en lugar de + y _ en lugar de /, y omite el carácter de relleno =.',
            'decodeb64.com detecta y maneja automáticamente la entrada Base64URL. Para inspeccionar un token JWT, pega el token completo o solo la parte del encabezado o carga útil.',
            'Ten en cuenta que decodificar un payload JWT revela los claims que contiene, pero no verifica la firma. Para validación de seguridad, siempre verifica la firma JWT con la librería adecuada.',
        ],
        's4_h2': 'Decodificar Archivos Base64 y Datos Binarios',
        's4_p': [
            'Para archivos codificados, decodeb64.com incluye una sección de decodificación de archivos que acepta archivos .txt codificados en Base64. Sube el archivo con la cadena Base64 y la herramienta lo decodificará al contenido binario original. El tipo de archivo se detecta automáticamente usando firmas de bytes mágicos.',
            'Esto es útil para recuperar archivos codificados para transmisión por correo o respuestas API, extraer imágenes incrustadas como Base64 en archivos de configuración, y decodificar datos binarios almacenados en bases de datos.',
            'Recordatorio de seguridad: siempre verifica la fuente de los datos Base64 antes de decodificar y ejecutar archivos. Nunca ejecutes un archivo decodificado de una fuente no confiable.',
        ],
    },
    'pt/index.html': {
        'h1': 'Decodificador Base64 Online',
        's1_h2': 'O que é Decodificação Base64?',
        's1_p': [
            'A decodificação Base64 é o inverso da codificação Base64 — ela converte uma string Base64 de volta aos seus dados binários ou de texto originais. Dada uma string Base64 válida, qualquer decodificador pode reconstruir os dados originais sem nenhuma chave ou senha, por isso o Base64 não é uma forma de criptografia.',
            'Dados codificados em Base64 são comumente encontrados em tokens JWT, anexos de e-mail transmitidos via MIME, Data URIs de imagens incorporadas em HTML e CSS, dados binários retornados por APIs REST em respostas JSON, e arquivos de configuração que armazenam valores binários como texto.',
            'Ao decodificar, é importante conhecer a codificação de caracteres original. Se o texto original era UTF-8, selecionar UTF-8 ou AUTO-DETECT produzirá resultados corretos.',
        ],
        's2_h2': 'Como Decodificar Base64 Online',
        's2_p': [
            'Para decodificar uma string Base64 com decodeb64.com, cole sua string codificada no campo de entrada e clique em Decodificar. A ferramenta remove automaticamente espaços e quebras de linha antes de decodificar.',
            'Se você estiver decodificando uma string Base64URL (que usa - e _ em vez de + e /), a ferramenta lida com isso automaticamente. Se a codificação de caracteres for desconhecida, selecione AUTO-DETECT.',
            'Para decodificação em lote, ative "Decodificar cada linha separadamente" — cada linha será decodificada de forma independente, útil para listas de tokens ou identificadores codificados.',
        ],
        's3_h2': 'Decodificar Base64URL e Tokens JWT',
        's3_p': [
            'JWTs (JSON Web Tokens) consistem em três partes separadas por pontos: cabeçalho.payload.assinatura. O cabeçalho e o payload são codificados em Base64URL — não em Base64 padrão. Base64URL usa - em vez de + e _ em vez de /, e omite o caractere de preenchimento =.',
            'decodeb64.com detecta e lida automaticamente com a entrada Base64URL. Para inspecionar um token JWT, cole o token completo ou apenas a parte do cabeçalho ou payload.',
            'Observe que decodificar um payload JWT revela os claims que ele contém, mas não verifica a assinatura. Para validação de segurança, sempre verifique a assinatura JWT com a biblioteca adequada.',
        ],
        's4_h2': 'Decodificar Arquivos Base64 e Dados Binários',
        's4_p': [
            'Para arquivos codificados, decodeb64.com inclui uma seção de decodificação de arquivos que aceita arquivos .txt codificados em Base64. Faça upload do arquivo com a string Base64 e a ferramenta o decodificará de volta ao conteúdo binário original. O tipo de arquivo é detectado automaticamente usando assinaturas de bytes mágicos.',
            'Isso é útil para recuperar arquivos codificados para transmissão por e-mail ou respostas de API, extrair imagens incorporadas como Base64 em arquivos de configuração.',
            'Lembrete de segurança: sempre verifique a fonte dos dados Base64 antes de decodificar e executar arquivos. Nunca execute um arquivo decodificado de uma fonte não confiável.',
        ],
    },
    'fr/index.html': {
        'h1': 'Décodeur Base64 en Ligne',
        's1_h2': "Qu'est-ce que le décodage Base64 ?",
        's1_p': [
            "Le décodage Base64 est l'inverse de l'encodage Base64 — il convertit une chaîne Base64 en ses données binaires ou textuelles d'origine. Étant donné une chaîne Base64 valide, tout décodeur peut reconstruire les données d'origine sans aucune clé ni mot de passe, c'est pourquoi Base64 n'est pas une forme de chiffrement.",
            "Les données encodées en Base64 se rencontrent couramment dans les tokens JWT, les pièces jointes d'e-mail transmises via MIME, les Data URI d'images intégrées dans HTML et CSS, les données binaires retournées par les API REST dans des réponses JSON, et les fichiers de configuration qui stockent des valeurs binaires sous forme de texte.",
            "Lors du décodage, il est important de connaître l'encodage de caractères d'origine. Si le texte original était UTF-8, sélectionner UTF-8 ou AUTO-DETECT produira des résultats corrects.",
        ],
        's2_h2': 'Comment décoder du Base64 en ligne',
        's2_p': [
            "Pour décoder une chaîne Base64 avec decodeb64.com, collez votre chaîne encodée dans le champ de saisie et cliquez sur Décoder. L'outil supprime automatiquement les espaces et les sauts de ligne avant le décodage.",
            "Si vous décodez une chaîne Base64URL (qui utilise - et _ au lieu de + et /), l'outil gère cela automatiquement. Si l'encodage de caractères est inconnu, sélectionnez AUTO-DETECT.",
            'Pour le décodage par lots, activez "Décoder chaque ligne séparément" — chaque ligne sera décodée indépendamment, utile pour les listes de tokens ou d\'identifiants encodés.',
        ],
        's3_h2': 'Décoder Base64URL et les tokens JWT',
        's3_p': [
            "Les JWT (JSON Web Tokens) sont composés de trois parties séparées par des points : en-tête.charge_utile.signature. L'en-tête et la charge utile sont encodés en Base64URL — pas en Base64 standard. Base64URL utilise - au lieu de + et _ au lieu de /, et omet le caractère de rembourrage =.",
            "decodeb64.com détecte et gère automatiquement l'entrée Base64URL. Pour inspecter un token JWT, collez le token complet ou seulement la partie en-tête ou charge utile.",
            "Notez que décoder un payload JWT révèle les claims qu'il contient, mais ne vérifie pas la signature. Pour la validation de sécurité, vérifiez toujours la signature JWT avec la bibliothèque appropriée.",
        ],
        's4_h2': 'Décoder des fichiers Base64 et des données binaires',
        's4_p': [
            "Pour les fichiers encodés, decodeb64.com inclut une section de décodage de fichiers qui accepte les fichiers .txt encodés en Base64. Téléchargez le fichier contenant la chaîne Base64 et l'outil le décodera vers le contenu binaire d'origine. Le type de fichier est détecté automatiquement en utilisant les signatures de bytes magiques.",
            "Ceci est utile pour récupérer des fichiers encodés pour la transmission par e-mail ou des réponses API, extraire des images incorporées en Base64 dans des fichiers de configuration.",
            "Rappel de sécurité : vérifiez toujours la source des données Base64 avant de décoder et d'exécuter des fichiers. N'exécutez jamais un fichier décodé provenant d'une source non fiable.",
        ],
    },
    'de/index.html': {
        'h1': 'Base64 Decoder Online',
        's1_h2': 'Was ist Base64-Dekodierung?',
        's1_p': [
            'Base64-Dekodierung ist das Gegenteil von Base64-Kodierung — sie wandelt einen Base64-String in die ursprünglichen Binär- oder Textdaten zurück. Bei einem gültigen Base64-String kann jeder Decoder die ursprünglichen Daten ohne Schlüssel oder Passwort rekonstruieren, weshalb Base64 keine Form der Verschlüsselung ist.',
            'Base64-kodierte Daten begegnen einem häufig in JWT-Tokens, E-Mail-Anhängen via MIME, Bild-Data-URIs in HTML und CSS, Binärdaten aus REST-API-JSON-Antworten und Konfigurationsdateien, die binäre Werte als Text speichern.',
            'Beim Dekodieren ist es wichtig, die ursprüngliche Zeichenkodierung zu kennen. Wenn der Originaltext UTF-8 war, liefert die Auswahl von UTF-8 oder AUTO-DETECT korrekte Ergebnisse.',
        ],
        's2_h2': 'So dekodieren Sie Base64 online',
        's2_p': [
            'Um einen Base64-String mit decodeb64.com zu dekodieren, fügen Sie Ihren kodierten String in das Eingabefeld ein und klicken Sie auf Dekodieren. Das Tool entfernt vor dem Dekodieren automatisch Leerzeichen und Zeilenumbrüche.',
            'Beim Dekodieren eines Base64URL-Strings (der - und _ statt + und / verwendet) wird dies automatisch gehandhabt. Wenn die Zeichenkodierung unbekannt ist, wählen Sie AUTO-DETECT.',
            'Für die Stapeldekodierung aktivieren Sie "Jede Zeile separat dekodieren" — jede Zeile wird unabhängig dekodiert, nützlich für Listen von kodierten API-Tokens oder Bezeichnern.',
        ],
        's3_h2': 'Base64URL und JWT-Token dekodieren',
        's3_p': [
            'JWTs (JSON Web Tokens) bestehen aus drei durch Punkte getrennten Teilen: Header.Payload.Signatur. Header und Payload sind Base64URL-kodiert — nicht Standard-Base64. Base64URL verwendet - statt + und _ statt /, und lässt das =-Auffüllzeichen weg.',
            'decodeb64.com erkennt und verarbeitet Base64URL-Eingaben automatisch. Zum Inspizieren eines JWT-Tokens fügen Sie den vollständigen Token oder nur den Header- oder Payload-Teil ein.',
            'Beachten Sie, dass das Dekodieren eines JWT-Payloads die enthaltenen Claims preisgibt, aber die Signatur nicht verifiziert. Verwenden Sie für die Sicherheitsvalidierung immer die entsprechende Bibliothek.',
        ],
        's4_h2': 'Base64-Dateien und Binärdaten dekodieren',
        's4_p': [
            'Für kodierte Dateien bietet decodeb64.com einen Datei-Dekodierungsbereich, der Base64-kodierte .txt-Dateien akzeptiert. Laden Sie die Datei mit dem Base64-String hoch, und das Tool dekodiert sie zurück zum ursprünglichen Binärinhalt. Der Dateityp wird automatisch anhand von Magic-Byte-Signaturen erkannt.',
            'Dies ist nützlich zum Wiederherstellen von Dateien, die für die Übertragung per E-Mail oder API-Antworten kodiert wurden, und zum Extrahieren von als Base64 eingebetteten Bildern in Konfigurationsdateien.',
            'Sicherheitshinweis: Überprüfen Sie immer die Quelle der Base64-Daten, bevor Sie Dateien dekodieren und ausführen. Führen Sie niemals eine dekodierte Datei aus einer nicht vertrauenswürdigen Quelle aus.',
        ],
    },
    'it/index.html': {
        'h1': 'Decodificatore Base64 Online',
        's1_h2': "Cos'è la Decodifica Base64?",
        's1_p': [
            "La decodifica Base64 è l'inverso della codifica Base64 — converte una stringa Base64 nei suoi dati binari o testuali originali. Data una stringa Base64 valida, qualsiasi decoder può ricostruire i dati originali senza alcuna chiave o password, ecco perché Base64 non è una forma di crittografia.",
            'I dati codificati in Base64 si incontrano comunemente nei token JWT, negli allegati e-mail trasmessi via MIME, nei Data URI di immagini incorporati in HTML e CSS, nei dati binari restituiti da API REST in risposte JSON, e nei file di configurazione che memorizzano valori binari come testo.',
            "Durante la decodifica, è importante conoscere la codifica dei caratteri originale. Se il testo originale era UTF-8, selezionare UTF-8 o AUTO-DETECT produrrà risultati corretti.",
        ],
        's2_h2': 'Come decodificare Base64 online',
        's2_p': [
            'Per decodificare una stringa Base64 con decodeb64.com, incolla la tua stringa codificata nel campo di input e clicca su Decodifica. Lo strumento rimuove automaticamente spazi e a capo prima di decodificare.',
            'Se stai decodificando una stringa Base64URL (che usa - e _ invece di + e /), lo strumento lo gestisce automaticamente. Se la codifica dei caratteri è sconosciuta, seleziona AUTO-DETECT.',
            'Per la decodifica batch, abilita "Decodifica ogni riga separatamente" — ogni riga verrà decodificata in modo indipendente, utile per liste di token o identificatori codificati.',
        ],
        's3_h2': 'Decodificare Base64URL e Token JWT',
        's3_p': [
            'I JWT (JSON Web Token) sono composti da tre parti separate da punti: intestazione.payload.firma. L\'intestazione e il payload sono codificati in Base64URL — non in Base64 standard. Base64URL usa - invece di + e _ invece di /, e omette il carattere di padding =.',
            'decodeb64.com rileva e gestisce automaticamente l\'input Base64URL. Per ispezionare un token JWT, incolla il token completo o solo la parte dell\'intestazione o del payload.',
            'Tieni presente che decodificare un payload JWT rivela i claim che contiene, ma non verifica la firma. Per la validazione di sicurezza, usa sempre la libreria appropriata.',
        ],
        's4_h2': 'Decodificare file Base64 e dati binari',
        's4_p': [
            'Per i file codificati, decodeb64.com include una sezione di decodifica file che accetta file .txt codificati in Base64. Carica il file con la stringa Base64 e lo strumento lo decodificherà al contenuto binario originale. Il tipo di file viene rilevato automaticamente dai magic byte.',
            'Questo è utile per recuperare file codificati per la trasmissione via e-mail o risposte API, estrarre immagini incorporate come Base64 in file di configurazione.',
            "Promemoria sulla sicurezza: verifica sempre la fonte dei dati Base64 prima di decodificare ed eseguire file. Non eseguire mai un file decodificato da una fonte non attendibile.",
        ],
    },
    'zh/index.html': {
        'h1': 'Base64 在线解码器',
        's1_h2': '什么是 Base64 解码？',
        's1_p': [
            'Base64 解码是 Base64 编码的逆过程——它将 Base64 字符串转换回原始的二进制或文本数据。给定一个有效的 Base64 字符串，任何解码器都可以在没有任何密钥或密码的情况下重建原始数据，这就是为什么 Base64 不是一种加密形式。',
            'Base64 编码的数据常见于：JWT 令牌（其中标头和负载使用 Base64URL 编码）、通过 MIME 传输的电子邮件附件、嵌入 HTML 和 CSS 的图片 Data URI、REST API 在 JSON 响应中返回的二进制数据，以及将二进制值存储为文本的配置文件。',
            '解码时，了解文本数据的原始字符编码非常重要。如果原始文本是 UTF-8（最常见的情况），选择 UTF-8 或自动检测将产生正确结果。',
        ],
        's2_h2': '如何在线解码 Base64',
        's2_p': [
            '要使用 decodeb64.com 解码 Base64 字符串，请将编码后的字符串粘贴到输入框中，然后点击"解码"。该工具在解码前会自动去除空格和换行符，无需手动清理字符串。',
            '如果您正在解码 Base64URL 字符串（使用 - 和 _ 代替 + 和 /），工具会自动处理。如果字符编码未知，请选择自动检测。',
            '对于批量解码，启用"逐行解码"选项——每行将被独立解码，适用于多个 Base64 条目的列表。',
        ],
        's3_h2': '解码 Base64URL 和 JWT 令牌',
        's3_p': [
            'JWT（JSON Web Token）由三个用点分隔的部分组成：标头.负载.签名。标头和负载使用 Base64URL 编码——而非标准 Base64。Base64URL 使用 - 代替 +，_ 代替 /，并省略 = 填充字符。',
            'decodeb64.com 会自动检测并处理 Base64URL 输入。要检查 JWT 令牌，请粘贴完整令牌或仅粘贴标头或负载部分。',
            '请注意，解码 JWT 负载会显示其中包含的声明，但不会验证签名。对于安全验证，请始终使用适当的库验证 JWT 签名。',
        ],
        's4_h2': '解码 Base64 文件和二进制数据',
        's4_p': [
            '对于编码文件，decodeb64.com 提供文件解码部分，接受 Base64 编码的 .txt 文件。上传包含 Base64 字符串的文件，工具会将其解码回原始二进制内容。文件类型通过魔术字节签名从解码后的二进制中自动检测。',
            '这对于恢复通过电子邮件或 API 响应传输的编码文件、提取配置文件中嵌入的 Base64 图片非常有用。',
            '安全提醒：在解码和执行文件之前，请始终验证 Base64 数据的来源。切勿执行来自不受信任来源的解码文件。',
        ],
    },
    'ru/index.html': {
        'h1': 'Base64 Декодер Онлайн',
        's1_h2': 'Что такое декодирование Base64?',
        's1_p': [
            'Декодирование Base64 является обратным процессом кодирования Base64 — оно преобразует строку Base64 обратно в исходные бинарные или текстовые данные. При наличии корректной строки Base64 любой декодер может восстановить исходные данные без ключа или пароля, поэтому Base64 не является формой шифрования.',
            'Закодированные в Base64 данные часто встречаются в JWT-токенах, вложениях электронной почты через MIME, Data URI изображений в HTML и CSS, бинарных данных из REST API в ответах JSON и конфигурационных файлах, хранящих бинарные значения в виде текста.',
            'При декодировании важно знать исходную кодировку символов текстовых данных. Если исходный текст был UTF-8, выбор UTF-8 или AUTO-DETECT даст правильные результаты.',
        ],
        's2_h2': 'Как декодировать Base64 онлайн',
        's2_p': [
            'Чтобы декодировать строку Base64 с помощью decodeb64.com, вставьте закодированную строку в поле ввода и нажмите «Декодировать». Инструмент автоматически удаляет пробелы и переносы строк перед декодированием.',
            'При декодировании строки Base64URL (использующей - и _ вместо + и /) инструмент обрабатывает это автоматически. Если кодировка символов неизвестна, выберите AUTO-DETECT.',
            'Для пакетного декодирования включите «Декодировать каждую строку отдельно» — каждая строка будет декодирована независимо, что удобно для списков токенов или идентификаторов.',
        ],
        's3_h2': 'Декодирование Base64URL и JWT-токенов',
        's3_p': [
            'JWT (JSON Web Tokens) состоят из трёх частей, разделённых точками: заголовок.полезная_нагрузка.подпись. Заголовок и полезная нагрузка закодированы в Base64URL — не в стандартном Base64. Base64URL использует - вместо + и _ вместо /, и не включает символ заполнения =.',
            'decodeb64.com автоматически определяет и обрабатывает входные данные Base64URL. Для проверки JWT-токена вставьте полный токен или только часть заголовка или полезной нагрузки.',
            'Обратите внимание, что декодирование полезной нагрузки JWT раскрывает содержащиеся в ней claims, но не проверяет подпись. Для проверки безопасности всегда используйте соответствующую библиотеку.',
        ],
        's4_h2': 'Декодирование файлов Base64 и бинарных данных',
        's4_p': [
            'Для закодированных файлов decodeb64.com включает раздел декодирования файлов, принимающий .txt файлы в кодировке Base64. Загрузите файл со строкой Base64, и инструмент декодирует его обратно в исходное бинарное содержимое. Тип файла автоматически определяется с помощью сигнатур magic bytes.',
            'Это полезно для восстановления файлов, закодированных для передачи по электронной почте или в ответах API, и извлечения изображений, встроенных как Base64 в конфигурационные файлы.',
            'Напоминание о безопасности: всегда проверяйте источник данных Base64 перед декодированием и запуском файлов. Никогда не запускайте декодированный файл из ненадёжного источника.',
        ],
    },
    'ja/index.html': {
        'h1': 'Base64 オンラインデコーダー',
        's1_h2': 'Base64デコードとは？',
        's1_p': [
            'Base64デコードはBase64エンコードの逆処理です — Base64文字列を元のバイナリまたはテキストデータに変換します。有効なBase64文字列があれば、どのデコーダーもキーやパスワードなしに元のデータを復元できます。そのためBase64は暗号化の一形態ではありません。',
            'Base64エンコードされたデータは以下の場所でよく見られます：JWTトークン（ヘッダーとペイロードがBase64URLエンコードされている）、MIME経由で送信されるメール添付ファイル、HTMLやCSSに埋め込まれた画像のData URI、REST APIのJSONレスポンスで返されるバイナリデータ、バイナリ値をテキストとして保存する設定ファイル。',
            'デコード時には、テキストデータの元の文字エンコーディングを知ることが重要です。元のテキストがUTF-8だった場合、UTF-8またはAUTO-DETECTを選択すると正しい結果が得られます。',
        ],
        's2_h2': 'Base64をオンラインでデコードする方法',
        's2_p': [
            'decodeb64.comでBase64文字列をデコードするには、エンコードされた文字列を入力フィールドに貼り付け、「デコード」をクリックしてください。ツールはデコード前に空白と改行を自動的に除去するため、手動でクリーニングする必要はありません。',
            'Base64URL文字列（+と/の代わりに-と_を使用）をデコードする場合、ツールが自動的に処理します。文字エンコーディングが不明な場合はAUTO-DETECTを選択してください。',
            'バッチデコードには「各行を個別にデコード」オプションを有効にしてください — 各行が独立してデコードされ、複数のBase64エントリのリストに便利です。',
        ],
        's3_h2': 'Base64URLとJWTトークンのデコード',
        's3_p': [
            'JWT（JSON Web Token）はドットで区切られた3つの部分から成ります：ヘッダー.ペイロード.署名。ヘッダーとペイロードはBase64URLエンコードされています — 標準のBase64ではありません。Base64URLは+の代わりに-、/の代わりに_を使用し、=パディングを省略します。',
            'decodeb64.comはBase64URL入力を自動的に検出して処理します。JWTトークンを検査するには、完全なトークンまたはヘッダーかペイロード部分のみを貼り付けてください。',
            'JWTペイロードをデコードするとそのclaimsが明らかになりますが、署名は検証されないことに注意してください。セキュリティ検証には常に適切なライブラリを使用してください。',
        ],
        's4_h2': 'Base64ファイルとバイナリデータのデコード',
        's4_p': [
            'エンコードされたファイルに対して、decodeb64.comはBase64エンコードされた.txtファイルを受け付けるファイルデコードセクションを提供しています。Base64文字列を含むファイルをアップロードすると、ツールが元のバイナリコンテンツにデコードします。ファイルタイプはマジックバイトシグネチャを使って自動的に検出されます。',
            'これはメールやAPIレスポンスの送信用にエンコードされたファイルの復元、設定ファイルにBase64として埋め込まれた画像の抽出に役立ちます。',
            'セキュリティの注意事項：ファイルをデコードして実行する前に、Base64データのソースを必ず確認してください。信頼できないソースからのデコードされたファイルは絶対に実行しないでください。',
        ],
    },
    'ko/index.html': {
        'h1': 'Base64 온라인 디코더',
        's1_h2': 'Base64 디코딩이란?',
        's1_p': [
            'Base64 디코딩은 Base64 인코딩의 역과정입니다 — Base64 문자열을 원래의 바이너리 또는 텍스트 데이터로 다시 변환합니다. 유효한 Base64 문자열이 있으면 어떤 디코더든 키나 비밀번호 없이 원본 데이터를 복원할 수 있습니다. 그래서 Base64는 암호화의 한 형태가 아닙니다.',
            'Base64로 인코딩된 데이터는 다음에서 자주 볼 수 있습니다: JWT 토큰, MIME을 통해 전송되는 이메일 첨부 파일, HTML과 CSS에 삽입된 이미지 Data URI, REST API의 JSON 응답에서 반환되는 바이너리 데이터, 바이너리 값을 텍스트로 저장하는 구성 파일.',
            '디코딩할 때 텍스트 데이터의 원래 문자 인코딩을 아는 것이 중요합니다. 원본 텍스트가 UTF-8이었다면 UTF-8 또는 AUTO-DETECT를 선택하면 올바른 결과가 나옵니다.',
        ],
        's2_h2': '온라인으로 Base64를 디코딩하는 방법',
        's2_p': [
            'decodeb64.com으로 Base64 문자열을 디코딩하려면 인코딩된 문자열을 입력 필드에 붙여넣고 디코딩 버튼을 클릭하세요. 도구는 디코딩 전에 자동으로 공백과 줄 바꿈을 제거합니다.',
            'Base64URL 문자열(+ 와 / 대신 - 와 _ 사용)을 디코딩하는 경우 도구가 자동으로 처리합니다. 문자 인코딩을 모르는 경우 AUTO-DETECT를 선택하세요.',
            '"각 줄을 개별적으로 디코딩" 옵션을 활성화하면 배치 디코딩이 가능합니다 — 각 줄이 독립적으로 디코딩되어 여러 Base64 항목 목록에 유용합니다.',
        ],
        's3_h2': 'Base64URL 및 JWT 토큰 디코딩',
        's3_p': [
            'JWT(JSON Web Token)는 점으로 구분된 세 부분으로 구성됩니다: 헤더.페이로드.서명. 헤더와 페이로드는 Base64URL로 인코딩되어 있습니다 — 표준 Base64가 아닙니다. Base64URL은 + 대신 -, / 대신 _를 사용하고 = 패딩 문자를 생략합니다.',
            'decodeb64.com은 Base64URL 입력을 자동으로 감지하고 처리합니다. JWT 토큰을 검사하려면 전체 토큰이나 헤더 또는 페이로드 부분만 붙여넣으세요.',
            'JWT 페이로드를 디코딩하면 포함된 클레임이 드러나지만 서명은 검증되지 않습니다. 보안 검증을 위해서는 항상 적절한 라이브러리로 JWT 서명을 확인하세요.',
        ],
        's4_h2': 'Base64 파일 및 바이너리 데이터 디코딩',
        's4_p': [
            'イン코딩된 파일의 경우 decodeb64.com은 Base64로 인코딩된 .txt 파일을 받는 파일 디코딩 섹션을 제공합니다. Base64 문자열이 담긴 파일을 업로드하면 도구가 원래 바이너리 콘텐츠로 디코딩합니다. 파일 유형은 매직 바이트 시그니처를 사용하여 자동으로 감지됩니다.',
            '이는 이메일이나 API 응답으로 전송하기 위해 인코딩된 파일을 복원하고, 구성 파일에 Base64로 삽입된 이미지를 추출하는 데 유용합니다.',
            '보안 알림: 파일을 디코딩하고 실행하기 전에 항상 Base64 데이터의 출처를 확인하세요. 신뢰할 수 없는 출처의 디코딩된 파일은 절대 실행하지 마세요.',
        ],
    },
    'nl/index.html': {
        'h1': 'Base64 Decoder Online',
        's1_h2': 'Wat is Base64-decodering?',
        's1_p': [
            'Base64-decodering is het omgekeerde van Base64-codering — het converteert een Base64-string terug naar de originele binaire of tekstgegevens. Met een geldige Base64-string kan elke decoder de originele gegevens reconstrueren zonder sleutel of wachtwoord, daarom is Base64 geen vorm van versleuteling.',
            'Base64-gecodeerde gegevens komen veel voor in JWT-tokens, e-mailbijlagen via MIME, afbeeldings-Data-URI\'s in HTML en CSS, binaire gegevens van REST API\'s in JSON-reacties, en configuratiebestanden die binaire waarden als tekst opslaan.',
            'Bij het decoderen is het belangrijk de originele tekencodering van de tekstgegevens te kennen. Als de originele tekst UTF-8 was, geeft het selecteren van UTF-8 of AUTO-DETECT correcte resultaten.',
        ],
        's2_h2': 'Hoe Base64 online decoderen',
        's2_p': [
            'Om een Base64-string te decoderen met decodeb64.com, plakt u uw gecodeerde string in het invoerveld en klikt u op Decoderen. Het hulpmiddel verwijdert automatisch spaties en regeleinden voor het decoderen.',
            'Bij het decoderen van een Base64URL-string (die - en _ gebruikt in plaats van + en /) wordt dit automatisch afgehandeld. Als de tekencodering onbekend is, selecteer dan AUTO-DETECT.',
            'Voor batchdecodering schakelt u "Elke regel afzonderlijk decoderen" in — elke regel wordt onafhankelijk gedecodeerd, handig voor lijsten met gecodeerde tokens of identifiers.',
        ],
        's3_h2': 'Base64URL en JWT-tokens decoderen',
        's3_p': [
            "JWT's (JSON Web Tokens) bestaan uit drie delen gescheiden door punten: header.payload.handtekening. De header en payload zijn Base64URL-gecodeerd — niet standaard Base64. Base64URL gebruikt - in plaats van + en _ in plaats van /, en laat het =-opvulteken weg.",
            'decodeb64.com detecteert en verwerkt Base64URL-invoer automatisch. Om een JWT-token te inspecteren, plakt u het volledige token of alleen het header- of payload-gedeelte.',
            'Merk op dat het decoderen van een JWT-payload de claims onthult, maar de handtekening niet verifieert. Gebruik voor beveiligingsvalidatie altijd de juiste bibliotheek.',
        ],
        's4_h2': 'Base64-bestanden en binaire gegevens decoderen',
        's4_p': [
            'Voor gecodeerde bestanden biedt decodeb64.com een bestandsdecoderingsgedeelte dat Base64-gecodeerde .txt-bestanden accepteert. Upload het bestand met de Base64-string en het hulpmiddel decodeert het terug naar de originele binaire inhoud. Het bestandstype wordt automatisch gedetecteerd met behulp van magic byte-handtekeningen.',
            'Dit is handig voor het herstellen van bestanden die zijn gecodeerd voor verzending via e-mail of API-reacties, en voor het extraheren van als Base64 ingebedde afbeeldingen in configuratiebestanden.',
            'Beveiligingsherinnering: controleer altijd de bron van Base64-gegevens voordat u bestanden decodeert en uitvoert. Voer nooit een gedecodeerd bestand uit van een niet-vertrouwde bron.',
        ],
    },
    'hi/index.html': {
        'h1': 'Base64 ऑनलाइन डिकोडर',
        's1_h2': 'Base64 डिकोडिंग क्या है?',
        's1_p': [
            'Base64 डिकोडिंग Base64 एन्कोडिंग का उल्टा है — यह Base64 स्ट्रिंग को उसके मूल बाइनरी या टेक्स्ट डेटा में वापस बदलता है। एक वैध Base64 स्ट्रिंग दिए जाने पर, कोई भी डिकोडर बिना किसी कुंजी या पासवर्ड के मूल डेटा को पुनर्निर्मित कर सकता है, यही कारण है कि Base64 एन्क्रिप्शन का एक रूप नहीं है।',
            'Base64 एन्कोडेड डेटा आमतौर पर JWT टोकन, MIME के माध्यम से ईमेल अटैचमेंट, HTML और CSS में एम्बेड इमेज Data URI, REST API के JSON रिस्पॉन्स में बाइनरी डेटा, और बाइनरी मान को टेक्स्ट के रूप में संग्रहीत करने वाली कॉन्फ़िगरेशन फ़ाइलों में पाया जाता है।',
            'डिकोड करते समय, टेक्स्ट डेटा की मूल कैरेक्टर एन्कोडिंग जानना महत्वपूर्ण है। यदि मूल टेक्स्ट UTF-8 था, तो UTF-8 या AUTO-DETECT चुनने से सही परिणाम मिलेंगे।',
        ],
        's2_h2': 'Base64 को ऑनलाइन कैसे डिकोड करें',
        's2_p': [
            'decodeb64.com से Base64 स्ट्रिंग डिकोड करने के लिए, अपनी एन्कोडेड स्ट्रिंग इनपुट फ़ील्ड में पेस्ट करें और डिकोड बटन क्लिक करें। टूल डिकोड करने से पहले स्वचालित रूप से व्हाइटस्पेस और लाइन ब्रेक हटा देता है।',
            'Base64URL स्ट्रिंग (जो + और / के बजाय - और _ उपयोग करती है) डिकोड करते समय, टूल इसे स्वचालित रूप से संभालता है। यदि कैरेक्टर एन्कोडिंग अज्ञात है, तो AUTO-DETECT चुनें।',
            'बैच डिकोडिंग के लिए "प्रत्येक पंक्ति को अलग से डिकोड करें" विकल्प सक्षम करें — प्रत्येक पंक्ति स्वतंत्र रूप से डिकोड होगी, एन्कोडेड टोकन या आइडेंटिफ़ायर की सूचियों के लिए उपयोगी।',
        ],
        's3_h2': 'Base64URL और JWT टोकन डिकोड करें',
        's3_p': [
            'JWT (JSON Web Token) तीन भागों से बने होते हैं जो डॉट से अलग होते हैं: हेडर.पेलोड.सिग्नेचर। हेडर और पेलोड Base64URL एन्कोडेड हैं — मानक Base64 नहीं। Base64URL + के बजाय - और / के बजाय _ का उपयोग करता है, और = पैडिंग कैरेक्टर को छोड़ देता है।',
            'decodeb64.com स्वचालित रूप से Base64URL इनपुट को डिटेक्ट और हैंडल करता है। JWT टोकन को जांचने के लिए, पूरा टोकन या केवल हेडर या पेलोड भाग पेस्ट करें।',
            'ध्यान दें कि JWT पेलोड को डिकोड करने से उसके क्लेम्स का पता चलता है, लेकिन सिग्नेचर वेरीफाई नहीं होता। सुरक्षा सत्यापन के लिए हमेशा उपयुक्त लाइब्रेरी से JWT सिग्नेचर वेरीफाई करें।',
        ],
        's4_h2': 'Base64 फ़ाइलें और बाइनरी डेटा डिकोड करें',
        's4_p': [
            'एन्कोडेड फ़ाइलों के लिए, decodeb64.com में एक फ़ाइल डिकोड सेक्शन है जो Base64-एन्कोडेड .txt फ़ाइलें स्वीकार करता है। Base64 स्ट्रिंग वाली फ़ाइल अपलोड करें, और टूल इसे मूल बाइनरी सामग्री में डिकोड कर देगा। फ़ाइल प्रकार magic byte signatures का उपयोग करके डिकोडेड बाइनरी से स्वचालित रूप से पहचाना जाता है।',
            'यह ईमेल या API रिस्पॉन्स में ट्रांसमिशन के लिए एन्कोड की गई फ़ाइलों को रिकवर करने और कॉन्फ़िगरेशन फ़ाइलों में Base64 के रूप में एम्बेड इमेज निकालने के लिए उपयोगी है।',
            'सुरक्षा अनुस्मारक: फ़ाइलों को डिकोड और निष्पादित करने से पहले हमेशा Base64 डेटा के स्रोत को सत्यापित करें। अविश्वसनीय स्रोत से डिकोड की गई फ़ाइल कभी निष्पादित न करें।',
        ],
    },
}

# Marker between FAQ end and Other Tools
FAQ_END_MARKER = '  <!-- OTHER TOOLS -->'
OLD_H1_PATTERN = '<h1 data-i18n="hero_h1">'

def make_sections(d):
    def card(h2, paragraphs):
        ps = '\n'.join(f'    <p style="margin:0 0 12px;">{p}</p>' for p in paragraphs)
        return f'''
  <section style="margin-top:28px;">
    <div class="glass-card" style="padding:24px 28px;">
      <h2 class="content-h2" style="margin-top:0;">{h2}</h2>
{ps}
    </div>
  </section>'''
    return (
        '\n  <!-- H2-SECTIONS -->' +
        card(d['s1_h2'], d['s1_p']) +
        card(d['s2_h2'], d['s2_p']) +
        card(d['s3_h2'], d['s3_p']) +
        card(d['s4_h2'], d['s4_p']) +
        '\n'
    )

for path, d in DATA.items():
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Update H1
    import re
    c = re.sub(r'(<h1 data-i18n="hero_h1">)[^<]*(</h1>)', rf'\g<1>{d["h1"]}\2', c)

    # 2. Insert H2 sections before <!-- OTHER TOOLS -->
    if '<!-- OTHER TOOLS -->' in c and '<!-- H2-SECTIONS -->' not in c:
        c = c.replace(FAQ_END_MARKER, make_sections(d) + FAQ_END_MARKER)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Updated: {path}')

print('Done!')

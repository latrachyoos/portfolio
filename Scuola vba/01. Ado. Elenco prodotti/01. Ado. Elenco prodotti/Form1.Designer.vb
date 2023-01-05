<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.cmbcategoria = New System.Windows.Forms.ComboBox()
        Me.dgv = New System.Windows.Forms.DataGridView()
        Me.NomeProdotto = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.PrezzoUnitario = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.Categoria = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.Scorte = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.LivelloDiRiordino = New System.Windows.Forms.DataGridViewTextBoxColumn()
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'cmbcategoria
        '
        Me.cmbcategoria.FormattingEnabled = True
        Me.cmbcategoria.Location = New System.Drawing.Point(12, 12)
        Me.cmbcategoria.Name = "cmbcategoria"
        Me.cmbcategoria.Size = New System.Drawing.Size(132, 21)
        Me.cmbcategoria.TabIndex = 0
        Me.cmbcategoria.Text = "Seleziona la categoria"
        '
        'dgv
        '
        Me.dgv.AllowUserToAddRows = False
        Me.dgv.AllowUserToDeleteRows = False
        Me.dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.dgv.Columns.AddRange(New System.Windows.Forms.DataGridViewColumn() {Me.NomeProdotto, Me.PrezzoUnitario, Me.Categoria, Me.Scorte, Me.LivelloDiRiordino})
        Me.dgv.Location = New System.Drawing.Point(150, 12)
        Me.dgv.Name = "dgv"
        Me.dgv.ReadOnly = True
        Me.dgv.Size = New System.Drawing.Size(572, 285)
        Me.dgv.TabIndex = 1
        '
        'NomeProdotto
        '
        Me.NomeProdotto.HeaderText = "Nome Prodotto"
        Me.NomeProdotto.Name = "NomeProdotto"
        Me.NomeProdotto.ReadOnly = True
        '
        'PrezzoUnitario
        '
        Me.PrezzoUnitario.HeaderText = "Prezzo Unitario"
        Me.PrezzoUnitario.Name = "PrezzoUnitario"
        Me.PrezzoUnitario.ReadOnly = True
        '
        'Categoria
        '
        Me.Categoria.HeaderText = "Categoria"
        Me.Categoria.Name = "Categoria"
        Me.Categoria.ReadOnly = True
        '
        'Scorte
        '
        Me.Scorte.HeaderText = "Scorte"
        Me.Scorte.Name = "Scorte"
        Me.Scorte.ReadOnly = True
        '
        'LivelloDiRiordino
        '
        Me.LivelloDiRiordino.HeaderText = "Livello Di Riordino"
        Me.LivelloDiRiordino.Name = "LivelloDiRiordino"
        Me.LivelloDiRiordino.ReadOnly = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(740, 318)
        Me.Controls.Add(Me.dgv)
        Me.Controls.Add(Me.cmbcategoria)
        Me.Name = "Form1"
        Me.Text = "Form1"
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub
    Friend WithEvents cmbcategoria As System.Windows.Forms.ComboBox
    Friend WithEvents dgv As System.Windows.Forms.DataGridView
    Friend WithEvents NomeProdotto As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents PrezzoUnitario As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents Categoria As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents Scorte As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents LivelloDiRiordino As System.Windows.Forms.DataGridViewTextBoxColumn

End Class
